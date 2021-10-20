# Automaton

* Higher priority is with lower number

* Automaton parameters in __init__ before superclass call, then 
parse_arguments() doesn't need to be overloaded

* If working without sockets initialize with:
    ll=lambda: None
    recvsock=lambda: None

* Use from scapy.all import * or from scapy.arch import * to
initialize the L2/L3 sockets used by the automaton. 

* If no sockets are to be used, initialize the automation as following:
SampleAutomaton(ll=lambda: None, recvsock=lambda: None)



## Decorators
* state : Defines state
* condition: Wait for state, trigger action or go to state 
* action: Bound to one or many conditions

## Methods to overload
* parse_arguments()
* master_filter()


