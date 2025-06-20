# Python by Example

by Branimir Georgiev [(www.codewithbranko.com)](https://www.codewithbranko.com)

This tutorial provides over 200 Python programming examples suitable for 
junior, intermediate, and senior developers. It covers topics ranging from 
basic Python syntax to advanced concepts such as SOLID principles, design 
patterns, and best practices.

Each example is designed to be self-contained and easy to understand, allowing 
you to run and modify the code directly in your IDE. The examples are organized 
into directories based on topics, making it easy to find what you're looking 
for.


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
without express permission from the author.
