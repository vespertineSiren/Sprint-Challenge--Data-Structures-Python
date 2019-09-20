import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# runtime: 1.3573722839355469 seconds
# names_1.sort()
# names_2.sort()
#
# tree = BinarySearchTree(names_1)
# for comp_name in names_2:
#     if comp_name in tree.value:
#         duplicates.append(comp_name)

#runtime: 0.019945859909057617 seconds
names_1.sort()
names_2.sort()
i = 0
j = 0
while i < len(names_1)-1 or j < len(names_2)-1:
    if names_1[i] == names_2[j]:
        duplicates.append(names_1[i])
        i += 1
        j += 1
    elif names_1[i] > names_2[j]:
        j += 1
    else:
        i += 1

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

