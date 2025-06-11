"""Entry point executed when running the package with -m."""
import sys
import os.path


def main():
    progname = sys.argv[0]
    sys.argv[:] = sys.argv[1:]
    sys.path.insert(0, os.path.dirname(progname))

    print('sys.argv =', sys.argv)


if __name__ == "__main__":
    main()
