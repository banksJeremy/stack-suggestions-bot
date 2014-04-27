import json
import logging
import sys

from pprintpp import pprint as pp

import stackexchange

from .bot import Bot


class Application(object):
    # XXX: maybe this should just be rolled into Bot
    def __init__(self, settings):
        self._settings = settings

        self._init_irc()
        self._init_se()

    def _init_se(self):
        se_key = self._settings['stackexchange']['key']
        se_site = self._settings['stackexchange']['site']

        self._stack = stackexchange.StackExchange(se_key)
        self.site = self._stack.get_site(se_site)

    def _init_irc(self):
        self.bot = Bot(self)
