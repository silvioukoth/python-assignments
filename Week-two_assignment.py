my_list = []

my_list.extend([10, 20, 30, 40])

my_list.insert(1, 15)  # insert 15 at index 1 (second position)

my_list.extend([50, 60, 70])

my_list.pop() # removes the last element

my_list.sort() # sort in ascending order

index_of_30 = my_list.index(30)
print(index_of_30) #print the index of 30
print(my_list) #print the list