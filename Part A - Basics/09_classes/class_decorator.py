# Example: Class as decorator

# System imports
import logging
import functools


class Logger(object):
    log = logging.getLogger()
    """ Instance of a logging object"""

    logfile = ""
    """ Log file use to store the logs"""

    def __init__(self, logfile):

        Logger.logfile = logfile

        # logger instantiation
        log = logging.getLogger()
        Logger.log.setLevel(logging.INFO)

        # format output
        fmt = '%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s'
        formatter = logging.Formatter(fmt)

        # create the logging file handler
        fh = logging.FileHandler(Logger.logfile)
        fh.setFormatter(formatter)

        # add handler to logger object
        Logger.log.addHandler(fh)

    def __call__(self, function):
        """
        Wrapping call to original function.
        """

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            try:
                print("Calling function==[{0}]".format(function.__name__))
                return function(*args, **kwargs)

            except Exception as e:
                Logger.log.exception(e)

        return wrapper


@Logger("log.txt")
def f():
    print("Hello World")


f()
