from six.moves import input


class AppError(Exception):
    pass


class GameInput(object):

    def __init__(self, parser):
        self.parser = parser
        self.event = ""

    def wait(self):
        self.event = input('> ')
        return self


class GameLogic(object):

    def __init__(self, player, difficulty, attempts, category):
        self.player = player
        self.difficulty = difficulty
        self.attempts = attempts
        self.category = category
        self.score = 0
        self.show_guessed = False

    def update(self, user_input):

        if user_input.event == "quit":
            raise AppError("Quit game")

        elif user_input.event == "show_guess":
            self.show_guessed = True

        else:
            self.score += 1

        return self


class GameOutput(object):

    def __init__(self, show_guessed=True):
        self.show_guessed = show_guessed

    @staticmethod
    def show(state):

        for parameter in vars(state):
            print(parameter, getattr(state, parameter))


class GameApp(object):

    def __init__(self,
                 game_input,            # Class used to read the user input
                 game_output,           # Class used to generate the user output
                 game_logic,            # Class used to calculate the game state
                 use_cyrillic=False,    # Input parameter
                 difficulty=1,          # Logic parameter
                 attempts=20,           # Logic parameter
                 category="birds",      # Logic parameter
                 player="NEMO",         # Logic parameter
                 show_guessed=False,    # Output parameter
                 ):

        # Use the given class, create and configure input object
        self.game_input = game_input(parser=None)

        # Use the given class, create and configure output object
        self.game_output = game_output(
            show_guessed=show_guessed
        )

        # Use the given class, create and configure game logic object
        self.game_logic = game_logic(
            player,
            difficulty,
            attempts,
            category,
        )

    def run(self):
        while True:
            try:
                event = self.game_input.wait()
                state = self.game_logic.update(event)
                self.game_output.show(state)
            except AppError as e:
                break


if __name__ == "__main__":

    # Configure the game
    game = GameApp(
        game_input=GameInput,
        game_logic=GameLogic,
        game_output=GameOutput
    )

    # Start the game
    game.run()
