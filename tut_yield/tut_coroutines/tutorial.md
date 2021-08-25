# COROUTINE TUTORIAL

## Table of contents
_______________________________________________________________________________________________________________________

* [Overview](#overview)
  * [Coroutine Execution](#coroutine-syntax)
  * [Coroutine Chaining](#coroutine-chaining)
* [Comparison](#python-coroutine)
   * [Coroutine vs Subroutine](#coroutine-vs-subroutine)
   * [Coroutine vs Thread](#coroutine-vs-thread)
* [Usecases](#usecases)
* [Resources](#resources)


## Overview
_______________________________________________________________________________________________________________________

Coroutines are a special type of generator functions and represent generalizations of subroutines. They are used for 
**cooperative multitasking** where a process voluntarily yields (gives away) control periodically or when idle in 
order to enable multiple applications to be run simultaneously. Typically they are used to wait for a signal from 
another subroutine or coroutine to resume its execution.


### Coroutine Execution

     def coroutine():
        print("Coroutine has been started!")
        output = "foo"
        while True:
            text = yield output
            print("Coroutine input :", text)
            output = text[::-1] if text else "boo"
     
     
     cr = coroutine()

     # First usage of next to activate the coroutine and generate a default value
     print("Coroutine оutput : {0}".format(next(cr)))
     
     # Second usage of next to generate a new value
     print("Coroutine оutput : {0}".format(next(cr)))

     # Send data to the coroutine and generate a new value
     print("Coroutine оutput : {0}".format(cr.send("abc"))) 


     # Output:
     # -------------------------------
     # Coroutine has been started!
     # Coroutine оutput : foo
     # ('Coroutine received :', None)
     # Coroutine оutput : boo
     # ('Coroutine received :', 'abc')
     # Coroutine оutput : cba


The first usage of `next()` will activate the coroutine, print `Coroutine has been started!`, initialize the 
output and start the loop. The first result will be generated when the loop reaches the `yield output` expression. 

The second usage of next will resume the coroutine with the first statement after `yield`. As `next()` doesn't 
send any data the couroutine will print `('Coroutine received :', None)`. Next the output value is changed and the 
while loop is executed again. When the coroutine reaches the yield statment it will generate an output with the 
`yield output` expression.

Next the send method of generator functions is used to send data to the coroutine. The `text = yield ...` captures 
the value sent and the first statement after yield is executed. In this case the coroutine will print `
('Coroutine received :', 'abc')`. The output is then changed to take the reverse value of the input. Then the while 
loop is executed again and the new output is generated with the `yield output` expression.


### Coroutine Chaining

Coroutines can be used to set pipes. We can chain together coroutines and push data through the pipe using the `send()` 
method. A pipe needs at least the following

1. An initial source or producer
2. A sink or consumer


     def producer(string, next_coroutine):
         tokens = string.split(" ")
         for token in tokens:
             next_coroutine.send(token)
         next_coroutine.close()
     
     
     def consumer():
         print("I'm sink, i'll print tokens")
         try:
             while True:
                 token = (yield)
                 print(token)
         except GeneratorExit:
             print("Done with printing!")
     
     
     sentence = "Hello world!"
     print(sentence)
     
     # Define token printer (sink) and activate
     printer = consumer()
     next(printer)
     
     # Define token splitter (producer)
     producer(string=sentence, next_coroutine=printer)

     # Output
     # ---------------------------
     # Hello world!
     # I'm sink, i'll print tokens
     # Hello
     # world!
     # Done with printing!


## Comparions
_______________________________________________________________________________________________________________________

### Coroutine vs Subroutine

* Coroutines can be suspended and resumed
* Couritines can be resumed from many places
* Coroutines require cooperation by the calling application


### Coroutine vs Thread

* Threads are managed by the operating system
* Coroutines are managed by the program and the programming language


## Usecases
_______________________________________________________________________________________________________________________

1. Pipelines used to filter or to map objects
2. Finite state machines
3. Event handling
4. Milti-tasking
5. Callbacks replacement

## Excercises
_______________________________________________________________________________________________________________________

1. Write a simple coroutine which sends and receives data
2. Write a program which stops a coroutine
3. Write a simple decorator to activate a coroutine
4. Write a coroutine which computes the running average
6. Write a random bitstream generator 
7. Write a pipeline
8. Write simple finite state machine
9. Write a program to generate permutations using recursive coroutines
10. Write a simple multi-tasking OS using coroutines


## Resources
_______________________________________________________________________________________________________________________

* https://www.geeksforgeeks.org/coroutine-in-python/
* https://www.python-course.eu/python3_generators.php
* https://www.youtube.com/watch?v=EnSu9hHGq5o

