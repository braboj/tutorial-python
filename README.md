# Awesome Python!

by Branimir Georgiev, Vasil Andreev, Yorden Dragnev, Hristyan Grigorov, and others.

## Table of Contents

- [1. Getting Started](#getting-started)
    - [1.1. Install the prerequisites](#install-the-prerequisites)
    - [1.2. Clone the repository](#clone-the-repository)
    - [1.3. Open the project in PyCharm ](#open-the-project-in-pycharm)
    - [1.4. Install the AsciiDoc plugin](#install-the-asciidoc-plugin)
    - [1.5. Install asciidoctor (optional)](#install-asciidoctor-optional)

- [2. Project Description](#project-description)
    - [2.1. Project Purpose](#project-purpose)
    - [2.2. Project Structure](#project-structure)

- [3. Project Conventions](#project-conventions)
    - [3.1. File Naming](#file-naming)
    - [3.2. Commit Messages](#commit-messages)
    - [3.3. Issue Naming](#issue-naming)
    - [3.4. Pull Requests](#pull-requests)

## 1. Getting Started

### 1.1. Install the prerequisites
<a id='install-the-prerequisites'></a>

* [Python 3.10 or higher](https://www.python.org/downloads/)
* [PyCharm Community Edition](https://www.jetbrains.com/pycharm/)

### 1.2. Clone the repository
<a id='clone-the-repository'></a>

```
git clone https://github.com/braboj/tutorial-python.git
```

### 1.3. Open the project in PyCharm
<a id='open-the-project-in-pycharm'></a>

1. Open PyCharm
2. Select `File` -> `Open`
3. Navigate to the project folder
4. Select the `tutorial-python` folder

### 1.4. Install the AsciiDoc plugin
<a id='install-the-asciidoc-plugin'></a>

1. Click `Open`
2. Select `File` -> `Settings`
3. Select `Plugins`
4. Click `Marketplace`
5. Search for `AsciiDoc`
6. Click `Install`
7. Click `Restart IDE`

### 1.5. Install asciidoctor (optional)
<a id='install-asciidoctor-optional'></a>

1. Install Chocolatey (https://chocolatey.org/install)
2. Install ruby with `choco install ruby`
3. Install asciidoctor with `gem install asciidoctor`
4. Test with `asciidoctor --version`

## 2. Project Description
<a id="project-description"></a>

### 2.1. Project Purpose
<a id="project-purpose"></a>

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
 
### 2.2. Project Structure
<a id="project-structure"></a>

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
<a id="project-conventions"></a>

### 4.1. File Naming
<a id="file-naming"></a>

* `PART_<letter>.adoc` - Part file
* `CH_<number>.adoc` - Chapter file

### 4.2. Commit Messages
<a id="commit-messages"></a>

* (`#<id>`) - Use as a reference to a concrete issue number (either GitHub or JIRA)
* [`#####`] - No issue or ticket defined for this commit

**Examples**:
```
* (`#19`) - Add the operator precedence examples
* [`#####`] - Move the image assets to a dedicated folder
```

### 4.3. Issue Naming
<a id="issue-naming"></a>

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
<a id="pull-requests"></a>

- The requester is free to follow any style guide
- Preferably use https://blog.montrealanalytics.com/4-tips-for-effective-pull-request-naming-f60793998f04]


