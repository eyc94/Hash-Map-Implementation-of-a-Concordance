from hash_map import *
from word_count import top_words


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
m.put('key1', 9999)
m.put('key401', 9999)
m.put('key203', 9999)
m.put('dec', 1010)
print(m)

m.remove('key401')  # Removes key in the beginning.
print(m)
m.remove('key203')  # Removes key in the middle.
print(m)
m.remove('key1')  # Removes key in the end.
print(m)
m.remove('key1000')  # Attempts to remove non-existent key.
print(m)

m.put('key401', 401)
m.put('key203', 203)
m.put('key1', 1)
print(m)

print(m.get('key1'))  # Gets the value at the beginning.
print(m.get('key401'))  # Gets the value at the middle.
print(m.get('key104'))  # Gets the value at the end.
print(m.get('key234'))  # Gets a non-existent key.

print(m.contains_key('key1'))  # Checks first.
print(m.contains_key('key401'))  # Checks middle.
print(m.contains_key('key104'))  # Checks the end.
print(m.contains_key('key2340'))  # Checks non-existent.
print(m.contains_key('dec'))  # Checks single element.
print(m.empty_buckets())

print('resizing to 200!')
m.resize_table(200)
print(m)

print('------ cap 100 ------')
print(hash_function_1('dec') % 100)
print(hash_function_1('key30') % 100)
print(hash_function_1('key40') % 100)
print(hash_function_1('key50') % 100)
print(hash_function_1('key100') % 100)
print(hash_function_1('key1') % 100)
print(hash_function_1('key203') % 100)
print(hash_function_1('key302') % 100)
print(hash_function_1('key401') % 100)
print(hash_function_1('key104') % 100)
print(hash_function_1('key2') % 100)
print(hash_function_1('key207') % 100)

print('------ cap 200 ------')
print(hash_function_1('dec') % 200)
print(hash_function_1('key30') % 200)
print(hash_function_1('key40') % 200)
print(hash_function_1('key50') % 200)
print(hash_function_1('key100') % 200)
print(hash_function_1('key1') % 200)
print(hash_function_1('key203') % 200)
print(hash_function_1('key302') % 200)
print(hash_function_1('key401') % 200)
print(hash_function_1('key104') % 200)
print(hash_function_1('key2') % 200)
print(hash_function_1('key207') % 200)

print('------ cap 300 ------')
print(hash_function_1('dec') % 300)
print(hash_function_1('key30') % 300)
print(hash_function_1('key40') % 300)
print(hash_function_1('key50') % 300)
print(hash_function_1('key100') % 300)
print(hash_function_1('key1') % 300)
print(hash_function_1('key203') % 300)
print(hash_function_1('key302') % 300)
print(hash_function_1('key401') % 300)
print(hash_function_1('key104') % 300)
print(hash_function_1('key2') % 300)
print(hash_function_1('key207') % 300)


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



