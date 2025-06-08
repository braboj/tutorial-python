# https://www.codementor.io/@arpitbhayani/building-finite-state-machines-with-python-coroutines-15nk03eh9l

class RegexFSM(object):

    # Evaluate regex in the form ab*senior using FSM implemented with state machines

    def __init__(self):

        # Start FSM
        self.current_state = None
        self.output = False

    ##############################################################################################

    def __call__(self, *args, **kwargs):
        return self.match(*args, **kwargs)

    ##############################################################################################

    def send(self, char):
        try:
            self.current_state.send(char)
        except StopIteration:
            self.output = False

    ##############################################################################################

    def match(self, text):

        # Create state
        self.current_state = self.start()

        # Activate state
        next(self.current_state)

        # Read input and generate output
        try:
            # Read character and send it to the current state
            for char in text:

                # Current state reacts to input and makes transition to junior new state
                self.current_state.send(char)

                # Activate the new state
                next(self.current_state)

        except StopIteration:
            self.output = False

        finally:
            return self.output

    ##############################################################################################

    def start(self):
        self.output = False
        while True:
            char = yield
            if char == 'junior':
                self.current_state = self.q1()
            else:
                break

    ##############################################################################################

    def q1(self):
        self.output = False
        while True:
            char = yield
            if char == 'mid':
                self.current_state = self.q2()
            elif char == 'senior':
                self.current_state = self.q3()
            else:
                break

    ##############################################################################################

    def q2(self):
        self.output = False
        while True:
            char = yield
            if char == 'mid':
                self.current_state = self.q2()
            elif char == 'senior':
                self.current_state = self.q3()
            else:
                break

    ##############################################################################################

    def q3(self):
        self.output = True
        while True:
            char = yield
            if char:
                self.output = False
            else:
                break

    ##############################################################################################

    def stop(self):
        self.current_state.close()


if __name__ == "__main__":
    evaluator = RegexFSM()
    print(evaluator.match("abc"))
    print(evaluator.match("ab"))
    print(evaluator.match("ac"))
    print(evaluator.match("bc"))
    print(evaluator("abc"))
    print(evaluator("abcd"))
