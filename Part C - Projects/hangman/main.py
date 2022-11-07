class Hangman(object):

    def __init__(self,
                 input,
                 output,
                 logic,
                 show_guessed=False,
                 difficulty=1,
                 attempts=20,
                 category="birds",
                 player="NEMO",
                 ):

        self.game_input = input
        self.game_output = output
        self.game_logic = logic(
            player,
            difficulty,
            attempts,
            category,
        )

    def run(self):
        while True:
            user_input = self.game_input.wait()
            state = self.game_logic.update(user_input)
            self.game_output.show(state)
            pass


class GameLogic(object):

    def __init__(self, player, difficulty, attempts, category):
        self.__score = 0
        self.show_guessed = False

    def update(self, command):

        if command == "quit":
            raise Exception

        elif command == "show_guess":
            self.show_guessed = True

        else:
            self.__score += 1

        return self


class GameOutput(object):

    @staticmethod
    def show(state):
        print(state)


class GameInput(object):

    @staticmethod
    def wait():
        line = raw_input()
        return line


game = Hangman(
    input=GameInput,
    logic=GameLogic,
    output=GameOutput
)
game.run()
