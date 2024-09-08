# append()

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]


# extend()
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]


# insert() - Inserts an element at a specified position.
my_list = [1, 2, 3]
my_list.insert(1, 'a')
print(my_list)  # Output: [1, 'a', 2, 3]

# remove()
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]


# pop()  - Removes and returns the element at a specified position (default is the last element).
my_list = [1, 2, 3]
element = my_list.pop(1)
print(element)  # Output: 2
print(my_list)  # Output: [1, 3]


# clear()
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []


# index()
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1


# count()
my_list = [1, 2, 3, 2, 2]
count = my_list.count(2)
print(count)  # Output: 3


# sort()
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]

my_list.sort(reverse=True)
print(my_list)  # Output: [3, 2, 1]


# reverse()
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]
