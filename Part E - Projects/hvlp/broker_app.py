# encoding: utf-8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from components.broker import *
from components.logger import *


def main(ip='localhost', port=65432):

    # TODO: Enhance broker to allow configuration form the command line or configuration file

    configure_logger(level=logging.DEBUG)

    broker = HvlpBroker(
        ip_addr=ip,
        port=int(port),
        session=HvlpSession,
    )

    broker.run()


if __name__ == "__main__":
    main(*sys.argv[1:])
