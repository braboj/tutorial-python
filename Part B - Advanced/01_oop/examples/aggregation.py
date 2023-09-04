# Example : Composition with classes

class Engine(object):

    def __init__(self, engine_type, engine_model):
        self.engine_type = engine_type
        self.engine_model = engine_model

    def start(self):
        print("{} engine started".format(self.engine_type))

    def stop(self):
        print("{} engine stopped".format(self.engine_type))


class SoliddFuelEngine(Engine):

    def __init__(self, engine_model):
        super(SoliddFuelEngine, self).__init__("solid fuel", engine_model)


class LiquidFuelEngine(Engine):

    def __init__(self, engine_model):
        super(LiquidFuelEngine, self).__init__("liquid fuel", engine_model)


class Rocket(object):

    def __init__(self, engine):

        # This is aggregation: The rocket instance has an engine instance
        # but the engine instance can exist without the rocket instance
        self.engine = engine

    def launch(self):
        self.engine.start()


rocket1 = Rocket(SoliddFuelEngine("model 1"))
rocket1.launch()

rocket2 = Rocket(LiquidFuelEngine("model 2"))
rocket2.launch()

