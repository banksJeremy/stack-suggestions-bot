import json
import logging
import sys

from pprintpp import pprint as pp

import stackexchange


class Application(object):
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
        return NotImplemented


def main():
    logging.basicConfig(level=logging.DEBUG)

    sys.stderr.write("Reading settings from stdin\n")
    settings = json.load(sys.stdin)

    app = Application(settings)
    
    similar = app.site.get_similar("how do i install vm on ec2?")

    pp(similar)


if __name__ == '__main__':
    main()
