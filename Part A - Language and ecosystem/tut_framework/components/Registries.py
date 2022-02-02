import re
import types


class Registrar(type):
    """A meta class used to generate a list of all subclasses of
    a class"""

    def __init__(cls, name, bases, dct):
        super(Registrar, cls).__init__(name, bases, dct)
        cls.register(cls)

    @classmethod
    def list(mcs):
        for x in getattr(mcs, 'classes', tuple()):
            yield x

    @classmethod
    def register(mcs, cls):
        try:
            classes = mcs.classes
        except AttributeError:
            classes = mcs.classes = []

        classes.append(cls)


class Registry(dict):
    """A derived dictionary class to store key value pairs"""

    def __init__(self, name):
        dict.__init__(self)
        self.name = name

    def register(self, key, value):
        if value != self.setdefault(key, value):
            raise KeyError(
                "{name}: element {key}={value} already exists with value {existing}".format(
                    name=self.name, key=key,
                    value=value,
                    existing=self[key]))

    def unregister(self, key):
        try:
            self.pop(key)
        except KeyError:
            raise KeyError("{name}: key {key} does not exists".format(name=self.name, key=key))

    def getValueByKey(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            if default:
                return default
            else:
                raise KeyError("{name}: key {key} not found".format(name=self.name, key=key))

    def getKeyByValue(self, value, default=None):
        for key, v in self.items():
            if v == value:
                return key

        if default is None:
            raise ValueError("{name}: value {value} not found exists".format(name=self.name, value=value))
        else:
            return default

    def getValues(self):
        return self.values()

    def getKeys(self):
        return self.keys()


class ErrorCodeRegistry(Registry):
    """A registry to use for error codes"""

    def getErrorCodeByErrorName(self, errorname):
        return self.getKeyByValue(errorname)

    def getErrorNamebyErrorCode(self, errorcode):
        """Get the human readable name of an error code"""
        unsigned_errorcode = (0x100000000 + errorcode) & 0xFFFFFFFF
        return self.getValueByKey(errorcode, "Unknown error code ({code:#10x})".format(code=unsigned_errorcode))

    def registerErrorCode(self, name, code):
        self.register(code, name)

    def registerErrorCodes(self, dictionary, regexp, raise_on_doubles=True):
        """Scan a dictionary for keys matching the given regular expression
        and add them to the registry"""
        f = re.compile(regexp)

        for key, value in dictionary.items():
            if not f.match(key):
                continue

            if not type(value) in (types.IntType, types.LongType):
                continue

            try:
                self.registerErrorCode(key, value)

            except Exception as e:
                print(e)
                if raise_on_doubles:
                    raise


class CommStateRegistry(Registry):
    """A registry to use for communcation state"""

    def getCommStatCodebyName(self, commstatname):
        return self.getKeyByValue(commstatname)

    def getCommStatNamebyCode(self, commstatcode):
        """Get the human readable name of an error code"""
        return self.getValueByKey(commstatcode, "Unknown error code ({code:#10x})".format(code=commstatcode))

    def registerCommStatCode(self, commstatname, commstatcode):
        self.register(commstatcode, commstatname)

    def registerCommStatCodes(self, dictionary, regexp, raise_on_doubles=True):
        """Scan a dictionary for keys matching the given regular expression
        and add them to the registry"""
        f = re.compile(regexp)

        for key, value in dictionary.items():
            if not f.match(key):
                continue

            if not type(value) in (types.IntType, types.LongType):
                continue

            try:
                self.registerCommStatCode(key, value)

            except Exception as e:
                print(e)
                if raise_on_doubles:
                    raise
