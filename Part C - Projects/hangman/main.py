from six.moves import input


####################################################################################################
# ERRORS
####################################################################################################

class GameError(Exception):
    pass


####################################################################################################
# GAME CLASSES
####################################################################################################

# TODO: Add abstract class
class GameSession(object):

    def __init__(self):
        self.quit = False
        self.show_guessed = False
        self.player_name = 'Nemo'
        self.difficulty = 0
        self.attempts = 10
        self.category = 'animals'
        self.score = 0
        self.word = []
        self.guess = []

    @classmethod
    def from_json(cls, player_name):
        # TODO: Read session from JSON file using player name
        return cls()


# TODO: Add abstract class
class GameInput(object):

    def __init__(self, session):
        self.session = session

    def wait(self):

        user_input = input('> ')

        if user_input == "q":
            raise GameError("Game End")

        elif user_input == 'd':
            self.session.difficulty += 1

        elif user_input == 'a':
            self.session.attempts += 1

        elif user_input == 'c':
            self.session.category = 'cars'

        elif user_input == "s":
            self.session.show_guessed = True

        return self


# TODO: Add abstract class
class GameEngine(object):

    def __init__(self, session):
        self.session = session

    def update(self):
        self.session.score += 1
        return self


# TODO: Add abstract class
class GameOutput(object):

    def __init__(self, session):
        self.session = session

    def show(self):
        print(vars(self.session))


####################################################################################################
# GAME APP : Make different versions depending on input, output and engine
####################################################################################################

class GameApp(object):

    def __init__(self,
                 session: GameSession = None  # Session used to store the player details
                 ):

        # Create game session
        if not session:
            session = GameSession()

        self.game_input = GameInput(session)
        self.game_engine = GameEngine(session)
        self.game_output = GameOutput(session)

    def run(self):
        while True:
            try:
                self.game_input.wait()
                self.game_engine.update()
                self.game_output.show()
            except GameError:
                break


if __name__ == "__main__":
    game = GameApp()
    game.run()
