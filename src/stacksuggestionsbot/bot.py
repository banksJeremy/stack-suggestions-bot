import json
import logging
import sys
import os
import threading

import irc
import irc.bot

import stackexchange
import chatexchange.wrapper


logger = logging.getLogger(__name__)


class Bot(object):
    def __init__(self, settings):
        self._settings = settings

        logger.debug("Initializing Stack Exchange API client")
        self._init_site()
        any_chat_enabled = False

        logger.info("Initializing Stack Exchange Chat client")
        self._init_sec()

        logger.info("Initializing IRC client")
        self._init_irc()

        self.started = False

    def start(self):
        assert not self.started
        self.started = True

        if self.sec:
            logger.info("Starting SEC thread")
            threading.Thread(target=self.sec._start).start()

        if self.irc:
            logger.info("Starting IRC thread")
            threading.Thread(target=self.irc._start).start()

    def kill(self):
        logger.info("Killing bot")
        self.irc.disconnect()
        self.sec._chat.logout()
        del self.irc
        del self.sec

    def get_setting(self, *keys):
        env_key = 'SSB_' + '_'.join(str(k).upper() for k in keys)

        if env_key in os.environ:
            return os.environ[env_key]

        result = self._settings
        for k in keys:
            result = result[k]

        return result

    def _init_site(self):
        se_key = self.get_setting('stackexchange', 'key')
        se_site = self.get_setting('stackexchange', 'site')

        self._stackexchange = stackexchange.StackExchange(se_key)
        self.site = self._stackexchange.get_site(se_site)

    def _init_sec(self):
        email = self.get_setting('sec', 'email')
        password = self.get_setting('sec', 'password')
        host_id = self.get_setting('sec', 'host_id')
        room_id = str(self.get_setting('sec', 'room_id'))

        self.sec = SEC(
            email, password, host_id, room_id, self.handle_message)

    def _init_irc(self):
        host = self.get_setting('irc', 'server', 0)
        port = int(self.get_setting('irc', 'server', 1))
        nick = self.get_setting('irc', 'nick')
        try:
            password = self.get_setting('irc', 'password')
        except KeyError:
            password = None
        channel = self.get_setting('irc', 'channel')

        self.irc = IRC(
            host, port, nick, password, channel, self.handle_message)

    def handle_message(self, message):
        """
        Yields all messages to be sent in response to a given message.
        """

        similar = self.site.get_similar(message)

        if similar:
            yield "%s - %s" % (
                similar[0]['title'], similar[0]['link'])
        else:
            yield "Sorry, I found nothing."


class IRC(irc.bot.SingleServerIRCBot):
    def __init__(self, host, port, nick, password, channel, handle_message):
        self._handle_message = handle_message

        self.nick = nick
        self.channel = channel

        self._host = host
        self._port = port

    def _start(self):
        super(IRC, self).__init__(
            [(self._host, self._port)], self.nick, self.nick)

    def on_welcome(self, connection, event):
        connection.join(self.channel)

    def _on_disconnect(self, *a, **kw):
        sys.exit()
        return super(Bot, self)._on_disconnect(*a, **kw)

    def _on_kick(self, *a, **kw):
        self.disconnect()
        return super(Bot, self)._on_kick(*a, **kw)

    def on_pubmsg(self, connection, event):
        if self.nick not in event.source.nick:
            body = event.arguments[0]

            if body.startswith(self.nick):
                message = body[len(self.nick):]

                for reply_line in self._handle_message(message):
                    self.connection.notice(
                        self.channel,
                        "%s: %s" % (event.source.nick, reply_line))


class SEC(object):
    def __init__(self, email, password, host_id, room_id, handle_message):
        self._handle_message = handle_message

        self._email = email
        self._password = password
        self.host_id = host_id
        self.room_id = room_id

        self._chat = chatexchange.wrapper.SEChatWrapper(self.host_id)

    def _start(self):
        self._chat.login(self._email, self._password)
        self._chat.joinRoom(self.room_id)
        self._chat.watchRoom(self.room_id, self.on_se_message, 4)

    def on_se_message(self, message, chat):
        # TODO: be able to determine if message is addressing me
        from pprintpp import pprint as pprint
        pp(message)

