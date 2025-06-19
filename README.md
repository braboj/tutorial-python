# Python by Example

by Branimir Georgiev [(www.codewithbranko.com)](https://www.codewithbranko.com)

This tutorial offers a comprehensive set of examples for the Python programming
language for junior, intermediate, and advanced programmers. It covers
everything from the basics of Python syntax to advanced topics like
SOLID principles, design patterns, and best practices.

## Prerequisites

Ensure that the following tools are installed before setting up the project:

- **IDE of your choice** - PyCharm, Visual Studio Code, or any other Python IDE
- **Python 3.10+** - the examples rely on modern Python features
- **git** - to clone this repository

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/braboj/python-by-example.git
```

Change into the project directory:

```bash
cd python-by-example
```

For Linx and macOS, create a virtual environment and install the dependencies
using the following commands:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For Windows users, use the following commands to create a virtual environment
and install the dependencies:

```cmd
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

The examples are intented to be used with an IDE of your choice so that you can
run, debug, and modify them as needed. Just open the project in your IDE, and 
you can start exploring the examples.

```text
.python-by-example
├── .venv/                  # Virtual environment directory
├── examples/               # Directory containing all the examples
│   ├── A01_introduction/   # Introduction examples
│   │   ├── hello_world.py
```

You can also run the examples from the command line. For example, to run the 
`hello_world.py` example, use the following command:

```bash
python examples/A01_introduction/hello_world.py
```


## License

This project is proprietary software. Copying or distribution is prohibited 
without express permission from the author. See the [LICENSE](LICENSE) file for
more details.
