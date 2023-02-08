# encoding: utf-8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import logging
import sys
import os


def configure_logger(level=logging.DEBUG):

    logger = logging.getLogger()
    logger.setLevel(level)

    # Get the absoulte path of the executed file and split it into file name and file extension
    f_name, f_ext = os.path.splitext(sys.argv[0])

    # Get the file name and add the '.log' extension
    file_name = sys.argv[0].replace(f_ext, b'.log')

    # Logging format for files and console
    fmt = logging.Formatter(b"%(asctime)s %(levelname)-8s - %(name)s: %(message)s")

    # Console handler
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(fmt)
    logger.addHandler(stdout_handler)

    # Add the file handler
    file_handler = logging.FileHandler(filename=file_name, mode=b"w")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)
