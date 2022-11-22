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

    def __init__(self, player_name='ANONYMOUS'):
        self.quit = False
        self.show_guessed = False
        self.player_name = player_name
        self.difficulty = 0
        self.attempts = 10
        self.category = 'animals'
        self.score = 0
        self.word = []
        self.guess = []

    def exists(self):
        # TODO: Check if a file with the player name exists
        pass

    def load(self):
        # TODO: Load the player session from a file
        pass

    def store(self):
        # TODO: Save the player session in a file
        pass


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
                 player_name: str
                 ):

        session = GameSession(player_name)
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
