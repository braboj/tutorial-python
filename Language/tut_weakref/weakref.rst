The weakref module supports weak references to objects. A normal reference increments the reference count on the
object and prevents it from being garbage collected. This outcome is not always desirable, especially when a
circular reference might be present or when a cache of objects should be deleted when memory is needed. A weak
reference is a handle to an object that does not keep it from being cleaned up automatically.