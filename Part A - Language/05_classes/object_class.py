from pprint import pprint

print("Create an instance of the object class")
obj = object()

print("The type of the object is {0}".format(type(obj)))
print("The instance of class object has the following properties and methods...")
print(pprint(dir(obj)))