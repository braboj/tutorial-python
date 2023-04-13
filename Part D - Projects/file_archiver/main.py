from archiver.parser import *
from archiver.manager import *


def run_archiver():

    """ Application to coordinate the relationships between the modules."""

    algorithm, action, file_in, file_out = UserInput.parse()
    archiver = ArchiveManager()
    archiver.execute(
        algorithm=algorithm,
        action=action,
        file_in=file_in,
        file_out=file_out
    )
    archiver.report()


if __name__ == "__main__":
    run_archiver()
