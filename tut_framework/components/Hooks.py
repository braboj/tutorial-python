import logging


class Hook(object):
    log = logging.getLogger("Hook")
    hooks = []

    def __init__(self, event, func, **kwargs):
        self.event = event
        self.func = func
        self.kwargs = kwargs

    @classmethod
    def register(cls, event, func, **kwargs):
        cls.hooks.append(Hook(event, func, **kwargs))

    @classmethod
    def unregister(cls, func):
        for hook in cls.hooks:
            if hook.func == func:
                break
        else:
            raise ValueError("Not found")

        cls.hooks.remove(hook)

    def run(self, **kwargs):
        self.log.debug("Running func {0}".format(self.func.__name__))

        kwargs.update(self.kwargs)
        self.func(**(dict(kwargs, **self.kwargs)))

    @classmethod
    def event(cls, event, **kwargs):
        for hook in cls.hooks:
            if hook.event == event:
                hook.run(**kwargs)


registerHook = Hook.register
unregisterHook = Hook.unregister
runHooks = Hook.event
