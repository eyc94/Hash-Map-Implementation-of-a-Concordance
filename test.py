from hash_map import *


m = HashMap(100, hash_function_1)
m.put('key1', 1)
m.put('key2', 2)
m.put('key30', 30)
m.put('key50', 50)
m.put('key40', 40)
m.put('key100', 100)
m.put('key104', 104)
m.put('key203', 203)
m.put('key302', 302)
m.put('key401', 401)
m.put('key207', 207)
m.put('dec', 1010)
print(m)



# m.put('key1', 10)
# m.put('key2', 20)
# m.put('key1', 40)
# m.put('key5', 50)
# # m.remove('key1')
# # m.remove('key1')
# # m.remove('key5')
# # m.remove('asdf')
# # m.remove('key5')
# # m.remove('key2')

# print(m)
# print(m.size)
# # print(m.contains_key('key1'))
# # print(m.contains_key('key2'))
# # print(m.contains_key('key3'))
# # print(m.contains_key('key5'))

# # m2 = HashMap(10, hash_function_1)
# # print(m.contains_key('asdf'))

# m.resize_table(200)
# print(m)
# print(m.size)


# # hash = hash_function_1('key1')
# # index = hash % 100
# # print(index)

# # index = hash % 200
# # print(index)

# # m.clear()
# # print(m)

# print(m.get('key1'))
# print(m.get('key2'))
# print(m.get('key5'))
# print(m.empty_buckets())
# print(m.table_load())
# print(m.size)
# print(m.capacity)
# load = m.size/m.capacity
# print(load)



