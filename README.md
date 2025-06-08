# Awesome Python!

by Branimir Georgiev, Vasil Andreev, Yorden Dragnev, Hristyan Grigorov, and others.

## 1. Getting Started

### 1.1. Install the prerequisites

* [Python 3.10 or higher](https://www.python.org/downloads/)
* [PyCharm Community Edition](https://www.jetbrains.com/pycharm/)

### 1.2. Clone the repository

```
git clone https://github.com/braboj/tutorial-python.git
```

### 1.3. Open the project in PyCharm

1. Open PyCharm
2. Select `File` -> `Open`
3. Navigate to the project folder
4. Select the `tutorial-python` folder

### 1.4. Install the AsciiDoc plugin

1. Click `Open`
2. Select `File` -> `Settings`
3. Select `Plugins`
4. Click `Marketplace`
5. Search for `AsciiDoc`
6. Click `Install`
7. Click `Restart IDE`

## 2. Deploying the PDF file

### 2.1. Install ruby on Windows

1. Open a new terminal as administrator
2. Install Chocolatey (https://chocolatey.org/install)
3. Install ruby with `choco install ruby`

### 2.2. Install ruby on Linux

1. Install ruby with `sudo apt install ruby-full`
2. Test with `ruby --version`

### 2.3. Install asciidoctor

1. Restart or open a new terminal as administrator
2. Install asciidoctor with `gem install asciidoctor`
3. Test with `asciidoctor --version`

### 2.4. Install ascidoctor-pdf

1. Restart or open a new terminal as administrator
2. Install asciidoctor-pdf with `gem install asciidoctor-pdf --pre`
3. Test with `asciidoctor-pdf --version`

### 2.5. Generate the PDF file

1. Open a terminal
2. Navigate to the project folder
3. Run `asciidoctor-pdf --theme ./Assets/pdf/themes/my-theme.yml BOOK.adoc -o ./Build/AWESOME_PYTHON.pdf`
4. The PDF file is located in the root folder
5. Commit and tag the commit with the version number
5. Push the commit and the tag to GitHub
6. Create a release on GitHub


## 3. Project Description

### 3.1. Project Purpose

This tutorial offers a comprehensive tutorial for the Python programming language. The tutorial is
written in the **AsciiDoc** format. The tutorial is divided into five parts:

* Part A - Basic Python Programming
* Part B - Advanced Python Programming
* Part C - Expert Python Programming
* Part D - Roadmaps for further learning
* Part E - Snippets for common libraries and frameworks

The first three parts are covering the Python Programming language. The last two parts are 
covering the Python ecosystem. The tutorial is designed to be read in order. However, each part 
is self-contained and can be read separately.
 
### 3.2. Project Structure

```
ROOT
  ├───Assets
  │   ├───audio
  │   ├───images
  │   └───videos
  │  
  ├───Part A - Basics
  │   └───Chapter 01 - ...
  │       ├───assets
  │       ├───exercises
  │       ├───examples
  │       └───snippets
  │
  ├───Part B - Advanced
  ├───Part C - Expert
  ├───Part D - Roadmaps
  └───Part E - Libraries

```

## 4. Project Conventions

### 4.1. File Naming

* `PART_<letter>.adoc` - Part file
* `CH_<number>.adoc` - Chapter file

### 4.2. Commit Messages

* (`#<id>`) - Use as a reference to a concrete issue number (either GitHub or JIRA)
* [`#####`] - No issue or ticket defined for this commit

**Examples**:
```
* (`#19`) - Add the operator precedence examples
* [`#####`] - Move the image assets to a dedicated folder
```

### 4.3. Issue Naming

* [`<part>, <chapter>`] - <message>
* The square brackets define the context (optional)
* The context is connected to a place in the document
* The square brackets are omitted if no context is needed

**Examples**:
```
* [Part A, Ch. 1] - Do this (with context)
* Do that (without context)
```

### 4.4. Pull Requests

- The requester is free to follow any style guide
- Preferably use https://blog.montrealanalytics.com/4-tips-for-effective-pull-request-naming-f60793998f04]
