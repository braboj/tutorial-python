from __future__ import print_function
import pickle
try:
   import cPickle
   test_cPickle = True
except:
    test_cPickle = False
import json
import marshal
import timeit
import msgpack

iterations=100000
data="'avzvasdklfjhaskldjfhkweljrqlkjb*@&$Y)(!#&$G@#lkjabfsdflb(*!G@#$(GKLJBmnz,bv(PGDFLKJ'"

print("iterations=",iterations)
print("data=",data)

print ("==== DUMP ====")
print("Pickle:", pickle)
print(">>", timeit.timeit("pickle.dumps("+data+")","import pickle",number=iterations))

print("Json:", json.__version__)
print(">>",timeit.timeit("json.dumps("+data+")","import json",number=iterations))

if test_cPickle:
   print("cPickle:", cPickle.__version__)
   print(">>",timeit.timeit("pickle.dumps("+data+")","import cPickle as pickle",number=iterations))

print("Marshal:", marshal.version)
print(">>",timeit.timeit("marshal.dumps("+data+")","import marshal", number=iterations))

print("Msgpack:", msgpack.version)
print(">>", timeit.timeit("msgpack.packb("+data+")","import msgpack", number=iterations))

print()
print ("==== LOAD ====")

print("Pickle:")
print(">>", timeit.timeit("pickle.loads(x)","import pickle; x=pickle.dumps("+data+")",number=iterations))

print("Json:", json.__version__)
print(">>",timeit.timeit("json.loads(x)","import json; x=json.dumps("+data+")",number=iterations))

if test_cPickle:
   print("cPickle:", cPickle.__version__)
   print(">>",timeit.timeit("pickle.loads(x)","import cPickle as pickle; x=pickle.dumps("+data+")",number=iterations))

print("Marshal:", marshal.version)
print(">>",timeit.timeit("marshal.loads(x)","import marshal; x=marshal.dumps("+data+")", number=iterations))

print("Msgpack:", msgpack.version)
print(">>", timeit.timeit("msgpack.unpackb(x)","import msgpack; x=msgpack.packb("+data+")", number=iterations))