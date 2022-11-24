## Introduction
___________________________________________________________________________________________________

### Keywords

- **Statement**
- **Expression**
- **Function**
- **Parameter**
- **Variable**
- Comment
- Strings

### Hello, world!

The very first program we will write is the more or less the traditional 'Hello world'. It will 
just print the favorite phrase of all software developers on the screen. 

```python
print("Hello world!")
print(1 + 1)
```

Now if after evaluation of the code we will see that

- we tell the computer what to do
- and `print` is a pre-defined code ready to be used by the developer
- and `print` uses a value to show it on the screen 
- and the value used by print can be either pre-defined such as `'Hello, world!'`
- or take the result of operations such as `1 + 1`

If we elaborate further we will see that a program generally is a

- Sequence of commands called **statements**
- Each statement might consist of operations returning results called **expressions**
- Or each statement might use pre-defined code blocks called **functions** 
- And each function may be configurable by the user through **parameters**

The final goal of a software product is then ...

- To work the intended way
- To be testable
- To be easily usable 
- To be easily maintainable

### Declaring variables
Now let's modify our program a little bit to be more reusable. Now we make print to work with any 
text possible. For this purpose we will use a variable. A variable is a container for data, 
which can be reused many times in the program.

```python
text = 'Hello world!'
print(text)
```

In the code above the variable `text` is declared and initialized. After this it may be used 
many times in the program. Now you might ask that this is absolutely unnecessary to use 2 
lines of code instead of one. Let's give another example to demonstrate why variables are useful.
Let's print 5 identical messages on the screen ...

```python
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
```

Now if we want to change the message on the screen we have to change all the statements in the 
program above. If we use a variable to store the text, the changes will be only in first statement.

```python
text = 'Hello world!'
print(text)
print(text)
print(text)
print(text)
print(text)
```


### Variable types
Python has several pre-defined variables types such as

- Strings which holds characters
- Numbers which hold integers, complex and floating point numbers
- Booleans which can be either true or false
- None used to signify that a variable is declared but not initialized

The following code will print all variables values and their types supported by Python at the 
time of speaking. Remember that the language is constantly evolving and it might be necessary to 
check the official documentation for changes. The type of the variable in Python can be checked 
by using `type()`. 

```python
var = "Hello world!"
print(type(var), var)

var = 1
print(type(var), var)

var = 3.14
print(type(var), var)

var = 1 + 1j
print(type(var), var)

var = False
print(type(var), var)

var = None
print(type(var), var)
```

In the code above we can see that `print()` is configured with two parameters. The first one 
tells print to show the variable type on the screen and the second one the variable value. In 
Python `print()` supports an infinite amount of parameters.

We see the types of the variables, but they are preceeded by `class`. We defined earlier that 
variables are data containers, which can hold values. The class tells Python what type of data 
the variable stores and how Python can operate with the data.

The class concept can be demonstrated by first working with 2 integer numbers. In the example below 
Python analyses the code and deducts that a and b are integers and uses the integer class to 
check how to add them.

```python
a = 1
b = 1
print(a + b)
```

In the same way in the next example the code is analysed Python and deducts that now a and b are 
complex numbers and thus another type of data. In this case Python will use the addition 
operation for this data class.

```python
a = 1 + 1j
b = 1 + 1j
print(a + b)
```

## Practice

1. Print your name on the screen
2. Make the program in such a way that you can print different names 10 times
3. Add an integer and a floating point number
4. Show the type of the result of the addition of floating point number and an integer
5. Check the type of `print`
6. Check the type of `type`