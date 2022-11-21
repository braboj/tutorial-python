# COROUTINE TUTORIAL

## Table of contents
____________________________________________________________________________________________________

* [Overview](#overview)
  * [Coroutine Execution](#coroutine-syntax)
  * [Coroutine Chaining](#coroutine-chaining)
* [Comparison](#python-coroutine)
   * [Coroutine vs Subroutine](#coroutine-vs-subroutine)
   * [Coroutine vs Thread](#coroutine-vs-thread)
* [Usecases](#usecases)
* [Resources](#resources)


## Concept
____________________________________________________________________________________________________

Coroutines are a particular type of generator function and represent generalizations of 
subroutines.They are used for cooperative multitasking where a process voluntarily yields (gives 
away) control periodically or when idle to enable multiple applications to run simultaneously.
 Typically they are used to waiting for a signal from another subroutine or coroutine to resume 
its execution.


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
     # 1. Coroutine has been started!
     # 2. Coroutine оutput : foo
     # 3. ('Coroutine received :', None)
     # 4. Coroutine оutput : boo
     # 5. ('Coroutine received :', 'abc')
     # 6. Coroutine оutput : cba


1. The first usage of next() will activate the coroutine, print, initialize the output 
and start the loop. 

2. The first result will be generated when the loop reaches the yield 
output expression.

3. The second usage of next will resume the coroutine with the first statement after yield. 
As next() doesn't send any data the coroutine will print ('Coroutine received :', None).

4. The output value is changed and the while loop is executed again. When the coroutine reaches 
   the yield statement it will generate an output with the yield output expression.

5. The send method of generator functions is used to send data to the coroutine.The `text = yield 
   output` statement captures the value sent and the first statement after yield is executed. In 
   this case, the coroutine will print('Coroutine received :', 'abc').

6. The output is then changed to take the reverse value of the input. Then the while loop is 
   executed again and the new output is generated with the yield output expression.

### Coroutine Interface

| Method | Example             | Description                                            |
|--------|---------------------|--------------------------------------------------------|
| next   |   next(coroutine)   | Generate value from the coroutine                      |
| send   |  coroutine.send(..) | Send a value to the coroutine                          |
| close  | coroutine.close(..) | Stop the coroutine by sending a GeneratorExit signal   |
| throw  | coroutine.throw(..) | Throw an exception to the coroutine for the next yield |

    def letter_generator(text):
        print("Started")
        position = 0
        try:
            while True:
                try:
                    offset = yield text[position]
    
                    if offset is None:
                        position += 1
                    else:
                        position = offset
    
                except ValueError:
                    print("Value error on position = " + str(position))
    
        except GeneratorExit:
            print("Terminated")
    
    
    letter = letter_generator("abc")
    
    # Generate letters
    print(next(letter))
    print(next(letter))
    
    # Reset generator and generate letter
    print(letter.send(0))
    
    # Generate next letter
    print(next(letter))
    
    # Throw an exception to the generator
    print(letter.throw(ValueError))
    
    # Throw GeneratorExit to the generator
    letter.close()

    # Output
    # ----------------------
    # Started
    # a
    # b
    # a
    # b
    # Value error on position = 1
    # b
    # Terminated


### Coroutine Chaining

Coroutines can be used to set pipes. We can chain together coroutines and push data through the 
ipe using the `send()` method. A pipe needs at least the following

1. An initial source or producer
2. A sink or consumer


     def producer(string, next_coroutine):
         tokens = string.split(" ")
         for token in tokens:
             next_coroutine.send(token)
         next_coroutine.close()
     
     
     def consumer():
         print("I'm the sink, I'll print tokens")
         try:
             while True:
                 token = (yield)
                 print(token)
         except GeneratorExit:
             print("Done with printing!")
     
     
     sentence = "Hello, world!"
     print(sentence)
     
     # Define token printer (consumer) and activate
     printer = consumer()
     next(printer)
     
     # Define token splitter (producer)
     producer(string=sentence, next_coroutine=printer)

     # Output
     # ---------------------------
     # Hello, world!
     # I'm the sink, i'll print tokens
     # Hello
     # world!
     # Done with printing!


## Comparisons
____________________________________________________________________________________________________

### Coroutine vs Subroutine

* Coroutines can be suspended and resumed
* Coroutines can be resumed from many places
* Coroutines require cooperation by the calling application


### Coroutine vs Thread

* Threads are managed by the operating system
* Coroutines are managed by the program and the programming language


## Usecases
____________________________________________________________________________________________________

1. Pipelines used to filter or map objects
2. Finite state machines
3. Event handling
4. Multi-tasking
5. Callbacks replacement

## Exercises
____________________________________________________________________________________________________

1. Write a coroutine usage template
2. Write a simple decorator to activate a coroutine
3. Write a coroutine that computes the running average
4. Write a random configurable byte stream generator 
5. Write a pipeline
6. Write simple finite state machine
7. Write a program to generate permutations using recursive coroutines
8. Write a simple multi-tasking OS using coroutines


## Resources
____________________________________________________________________________________________________

* https://www.geeksforgeeks.org/coroutine-in-python/
* https://www.python-course.eu/python3_generators.php
* https://www.youtube.com/watch?v=EnSu9hHGq5o

