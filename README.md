# Awesome Python!

by Branimir Georgiev, Vasil Andreev, Yorden Dragnev, Hristyan Grigorov, and others.

## 1. Project Description

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
 
## 2. Project Structure

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

## 3. Project Conventions

### 3.1. File Naming

* `PART_<letter>.adoc` - Part file
* `CH_<number>.adoc` - Chapter file

### 3.2. Commit Messages

* (`#<id>`) - Use as a reference to a concrete issue number (either GitHub or JIRA)
* [`#####`] - No issue or ticket defined for this commit

**Examples**:
```
* (`#19`) - Add the operator precedence examples
* [`#####`] - Move the image assets to a dedicated folder
```

### 3.3. Issue Naming

* [`<part>, <chapter>`] - <message>
* The square brackets define the context (optional)
* The context is connected to a place in the document
* The square brackets are omitted if no context is needed

**Examples**:
```
* [Part A, Ch. 1] - Do this (with context)
* Do that (without context)
```

### 3.4. Pull Requests

- The requester is free to follow any style guide
- Preferably use https://blog.montrealanalytics.com/4-tips-for-effective-pull-request-naming-f60793998f04]


