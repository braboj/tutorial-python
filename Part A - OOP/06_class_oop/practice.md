# Why using classes and objects?

The object oriented programming offers a way to solve problems which can be require a state and
a definition of relationships. 

For example one classical problem is to write a program that must calculate how the temperature is
propagated when we heat an object.

![](start_heating.png)

The longer we keep the heating process the more the object will get heated until a certain 
temperature is reached. The heating is not instanious but a gradual process, with a heat wave
propagating through the material of the object. The material itself determines how quick the final
temperature will be reached.

![](heat_propagation.png)

One solution would be to write a function which will iterate through all the elements in the table
and calculate the momentary state for each element.

```
# Matrix with all the elements
table = [ ... ]

def calc_temp_propagation(table):
    
    for row
        
    

```