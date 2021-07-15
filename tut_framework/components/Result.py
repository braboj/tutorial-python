import Logger
import locale


class Result(object):

    def __init__(self):
        self.reason = None
        self.log = Logger.getLogger(self.__class__.__name__)

    def getReason(self):
        reason = self.reason

        if isinstance(reason, str):
            reason = reason.decode(locale.getpreferredencoding())

        elif not isinstance(reason, unicode):
            reason = reason

        return reason


class Failed(Result):
    def __init__(self, reason):
        super(Failed, self).__init__()
        self.reason = reason

    def __str__(self):
        return "Test FAILED"


class Passed(Result):
    def __str__(self):
        return "Test PASSED"


class Skipped(Result):
    def __init__(self, reason):
        super(Skipped, self).__init__()
        self.reason = reason

    def __str__(self):
        return "Test SKIPPED"