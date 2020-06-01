from hash_map import *


m = HashMap(100, hash_function_1)
m.put('key1', 10)
m.put('key2', 20)
m.put('key1', 40)
m.put('key5', 50)
print(m)
