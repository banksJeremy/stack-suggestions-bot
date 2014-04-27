import sys

from .application import *


def main():
    logging.basicConfig(level=logging.DEBUG)

    sys.stderr.write("Reading settings from stdin\n")
    settings = json.load(sys.stdin)

    app = Application(settings)

    similar = app.site.get_similar("how do i install vm on ec2?")

    pp([q['title'] for q in similar])

    print "Are there more?", similar.has_more


if __name__ == '__main__':
    main()
