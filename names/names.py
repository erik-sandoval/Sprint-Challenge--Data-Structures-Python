import time
from BST import BinarySearchTree


start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# the original run time complexity was O(n^2) because of the nest for loops, which per name of the
# 10000 name_1 iterated through name_2 10000 names.

name_list = BinarySearchTree('Random Name')
duplicates = []
for name_1 in names_1:
    name_list.insert(name_1)
for name_2 in names_2:
    if name_list.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
