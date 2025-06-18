# Aggregation: objects hold references to independent parts
# -----------------------------------------------------------------------------
# Aggregation occurs when one object keeps references to other, independent
# objects.  The referenced parts can exist on their own and are not owned by
# the aggregator.  Here the `Rocket` receives an `Engine` instance that can
# outlive the rocket itself.

class Engine(object):

    def __init__(self, engine_type, engine_model):
        self.engine_type = engine_type
        self.engine_model = engine_model

    def start(self):
        print("{} engine started".format(self.engine_type))

    def stop(self):
        print("{} engine stopped".format(self.engine_type))


class SolidFuelEngine(Engine):

    def __init__(self, engine_model):
        super(SolidFuelEngine, self).__init__("solid fuel", engine_model)


class LiquidFuelEngine(Engine):

    def __init__(self, engine_model):
        super(LiquidFuelEngine, self).__init__("liquid fuel", engine_model)


class Rocket(object):

    def __init__(self, engine):
        # This is aggregation: the Rocket keeps a reference to an Engine
        # that was created outside. The engine is not owned by the Rocket
        # and could be reused elsewhere or exist on its own.
        self.engine = engine

    def launch(self):
        self.engine.start()


rocket1 = Rocket(SolidFuelEngine("model 1"))
rocket1.launch()

rocket2 = Rocket(LiquidFuelEngine("model 2"))
rocket2.launch()
