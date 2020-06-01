from hash_map import *


m = HashMap(100, hash_function_1)
m.put('key1', 10)
m.put('key2', 20)
m.put('key1', 40)
m.put('key5', 50)
# m.remove('key1')
# m.remove('key1')
# m.remove('key5')
# m.remove('asdf')
# m.remove('key5')
# m.remove('key2')

print(m)
# print(m.contains_key('key1'))
# print(m.contains_key('key2'))
# print(m.contains_key('key3'))
# print(m.contains_key('key5'))

# m2 = HashMap(10, hash_function_1)
# print(m.contains_key('asdf'))

m.resize_table(200)
print(m)


hash = hash_function_1('key1')
index = hash % 100
print(index)

index = hash % 200
print(index)
