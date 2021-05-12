import weakref

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# References
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import weakref
#
#
# class ExpensiveObject:
#
#     def __del__(self):
#         print('(Deleting {})'.format(self))
#
#
# obj = ExpensiveObject()
# r = weakref.ref(obj)
#
# print('obj:', obj)
# print('ref:', r)
# print('r():', r())
#
# print('deleting obj')
# del obj
# print('r():', r())


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Reference callbacks
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))


def callback(reference):
    """Invoked when referenced object is deleted"""
    print('callback({!r})'.format(reference))


obj = ExpensiveObject()
r = weakref.ref(obj, callback)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Finalizing objects
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import weakref


# class ExpensiveObject:
#
#     def __del__(self):
#         print('(Deleting {})'.format(self))
#
#
# def on_finalize(*args):
#     print('on_finalize({!r})'.format(args))
#
#
# obj = ExpensiveObject()
# weakref.finalize(obj, on_finalize, 'extra argument')
#
# del obj


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Caching objects
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import gc


# from pprint import pprint
# import weakref
#
# gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
#
#
# class ExpensiveObject:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return 'ExpensiveObject({})'.format(self.name)
#
#     def __del__(self):
#         print('    (Deleting {})'.format(self))
#
#
# def demo(cache_factory):
#     # hold objects so any weak references
#     # are not removed immediately
#     all_refs = {}
#     # create the cache using the factory
#     print('CACHE TYPE:', cache_factory)
#     cache = cache_factory()
#     for name in ['one', 'two', 'three']:
#         o = ExpensiveObject(name)
#         cache[name] = o
#         all_refs[name] = o
#         del o  # decref
#
#     print('  all_refs =', end=' ')
#     pprint(all_refs)
#     print('\n  Before, cache contains:', list(cache.keys()))
#     for name, value in cache.items():
#         print('    {} = {}'.format(name, value))
#         del value  # decref
#
#     # remove all references to the objects except the cache
#     print('\n  Cleanup:')
#     del all_refs
#     gc.collect()
#
#     print('\n  After, cache contains:', list(cache.keys()))
#     for name, value in cache.items():
#         print('    {} = {}'.format(name, value))
#     print('  demo returning')
#     return
#
#
# demo(dict)
# print()
# demo(weakref.WeakValueDictionary)