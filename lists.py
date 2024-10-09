# Creating list
my_list = [1,2.0,3+4j,'Akhil']
print(my_list)

# It accepts heterogeneous items in to it

list_1 = [1,2,{4:5,1:2,7:8},(1,2,3),[4,5],{1,2,3,4,5,6,7}]
print(list_1)

# list manipulation
my_list = [5,4,3,2,1]

my_list.append(4) # append takes only one argument

my_list.extend([4,5,6]) # it takes onlt iterables (str,list,tuple,set,dict)

my_list.insert(0,9) # It will insert new element in specified index.  var.insert(index_num,element)

my_list.clear() # It clears everything in that list

my_list.pop(1) # By default it deletes last index element, if you need specific element to be removed give indx number

my_list.remove(1) # It will remove first occurance value

count = my_list.count(1) # In this we have to declare another variable to work this

position = my_list.index(1) # It checks the value at index of first occurance

my_list.reverse()# it reverses the list

my_list.sort()  # it sorts in ascending order

print(my_list)

#copy operator

'''There are two main copy operators in python Shallow copy and deep copy and here's the example
of using both copies and how does it affects originl list while copying '''

import copy # we need to import the copy module to work on copy

original = [2,3,[4,5,6]]

shallow_copy = copy.copy(original)

deep_copy = copy.deepcopy(original)

original[2][0] = 44 # If we modify original list shallow_copy also get's affected so go for deep copy

print('original copy', original)
print('shallowcopy',shallow_copy)
print('deepcopy',deep_copy) # Deep copy is the best apporach for copying objects or values


