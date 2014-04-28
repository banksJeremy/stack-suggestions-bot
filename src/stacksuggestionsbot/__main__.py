import json
import logging
import signal
import sys
import time

from pprintpp import pprint as pp

from .bot import Bot


logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)

    sys.stderr.write("Reading settings from stdin\n")
    settings = json.load(sys.stdin)

    def on_int(signal, frame):
        logger.info("Starting to kill bot")
        bot.kill()
        logger.info("Shutting down in a few seconds")
        time.sleep(3)
        sys.exit(0)

    bot = Bot(settings)

    signal.signal(signal.SIGINT, on_int)

    bot.start()

    while True:
        time.sleep(2)


if __name__ == '__main__':
    main()
