Table of contents
=================

<!--ts-->
   * [Generator](#overview)
     * [Generator vs Iterator](#generator-vs-iterator)
     * [Generator vs Collection](#generator-vs-collection)
   * [Usecases](#usecases)
   * [References](#references)
<!--te-->
   
# Generator
_______________________________________________________________________________________________________________________

The **yield** statement suspends the function’s execution and sends a value back to the caller, but retains its 
state so that it can be resumed. When resumed, the function continues execution immediately after the last yield run.
This allows its code to produce a series of values over time, rather than computing them at once and sending them 
back like a single list.

    # Implementation with a colllection
    def evens(stream):
       them = []
       for n in stream:
          if n % 2 == 0:
             them.append(n)
       return them

    # Implementaton with a generator
    def evens(stream):
        for n in stream:
            if n % 2 == 0:
                yield n

## Generator vs Iterator
_______________________________________________________________________________________________________________________
Generators are a subtype of iterators as they implement the iterator protocol. The **iter()** method of the iterator 
protocol can be implemented as generator. 

## Generator vs Collection
This is basically comparing memory vs complexity. Genea

Collections can be iterated many times without any limitations. Generators are one-time operations and produce a 
sequence of values. In order to produce the same sequence the generator function must be called again.

# Usecases
_______________________________________________________________________________________________________________________

1. Reduced memory
2. Infinite sequences

# References
_______________________________________________________________________________________________________________________
* https://www.python-course.eu/python3_generators.php
* https://www.youtube.com/watch?v=EnSu9hHGq5o