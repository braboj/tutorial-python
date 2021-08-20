Table of contents
=================

<!--ts-->
   * [Coroutine](#coroutine)
      * [Coroutine vs Subroutine](#coroutine-vs-subroutine)
      * [Coroutine vs Thread](#coroutine-vs-thread)
   * [Python Coroutine](#python-coroutine)
     * [Syntax](#syntax)
     * [Execution](#execution)
     * [Chaining](#chaining)
   * [Usecases](#usecases)
   * [References](#references)
<!--te-->

# Coroutine
_______________________________________________________________________________________________________________________

Coroutines are generalizations of subroutines. They are used for **cooperative multitasking** where a process 
voluntarily yields (gives away) control periodically or when idle in order to enable multiple applications to be run 
simultaneously.

## Coroutine vs Subroutine

| Subroutine                               | Coroutine                                |
| ------------------------------------     | ---------------------------------------- |
| ![](./assets/images/subroutine.png)      | ![](./assets/images/coroutine.png)       |



* Coroutines can suspend and resume its execution
* Couritines can be resumed from many places
* Coroutines require cooperation by the calling application

## Coroutine vs Thread

* Threads are managed by the operating system
* Coroutines are managed by the program and the programming language

## Coroutine vs Handler Class

* Handler Objects need a class and methods
* Handler Objects are slower
* 

# Python Coroutine
_______________________________________________________________________________________________________________________

## Syntax
Coroutines can produce and consume data. In Python 2.5, a slight modification to the yield statement was introduced, 
now yield can also be used as an expression:

```
    def coroutine():
        print("Coroutine has been started!")
        output = "foo"
        while True:
            text = yield output
            print("Coroutine received :", text)
            output = text[::-1] if text else "boo"
    
    
    cr = coroutine()
    print("Coroutine sent : {0}".format(next(cr)))          # 1. Activate the coroutine with next()
    print("Coroutine sent : {0}".format(next(cr)))          # 2. First call to the coroutine to get data with next()
    print("Coroutine sent : {0}".format(cr.send("abc")))    # 3. Second call to the coroutine to send data
```

The couroutine is resumed with the first statement after the **yield** keyword. The first usage of next will 
activate the coroutine, activate the loop and generate the first result. The second usage of next will activate the 
coroutine, evaluate data received with **text = yield ...**, generate the desired output and then send the data with 
**... yield output**.

## Execution
The execution of the coroutine is similar to the generator. When we call coroutine nothing happens, it runs only in 
response to the **next()** and **sends()** methods. The next() method activates the coroutine and the yield 
expression in the form **data = yield** will pause the coroutine until data is sent using the send() method.

## Chaining
Coroutines can be used to set pipes. We can chain together coroutines and push data through the pipe using send() 
method. A pipe needs :

1. An initial source(producer) derives the whole pipeline.
2. A sink, which is the endpoint of the pipe. A sink might collect all data and display it.

# Usecases
_______________________________________________________________________________________________________________________

1. Pipelines used to filter or to map objects
2. Finite state machines
3. Event handling
4. Milti-tasking

# Excercises
_______________________________________________________________________________________________________________________

1. Write a simple coroutine which sends and receives data
2. Write a program which stops a coroutine
3. Write a simple decorator to activate a coroutine
4. Write a coroutine which computes the running average
5. Write a coroutine which computes the fibonacci numbers
6. Write a random bitstream generator 
7. Write a pipeline
8. Write simple finite state machine
9. Write a program to generate permutations using recursive coroutines
10. Write a simple multi-tasking OS using coroutines


# References
* https://www.geeksforgeeks.org/coroutine-in-python/
* https://www.python-course.eu/python3_generators.php

