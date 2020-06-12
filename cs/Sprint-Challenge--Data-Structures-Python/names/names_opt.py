import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value: # If the value is less than the base value
            if not self.left: # If there's no left value
                self.left = BinarySearchTree(value) # Make given value the top left value
            else: # if it is left
                self.left.insert(value) # insert the new value
        else: # if the value is more than the base value
            if not self.right: # if there's no right value
                self.right = BinarySearchTree(value) # make given value the top right value
            else: # if it is right
                self.right.insert(value) # insert the new value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target: # If the top value == target
            return True # Return true

        if target < self.value: # If the target value is less than the top node
            if not self.left: # If there is no left values
                return False # Return false
            else: # If there is left values
                return self.left.contains(target) # Search the left for the target value
        else: # If the target value is more than the top node
            if not self.right: # If there's no right values
                return False # Return false
            else: # If there's right values
                return self.right.contains(target) # Search for the target value

duplicates = []
bst = BinarySearchTree(names_1[0]) # 0(n log n) no nested for loops using bts
for name in names_1: # for everyname in names_1
    bst.insert(name) # insert into bst
for name in names_2: # for eveeryname in names_2
    if bst.contains(name): # if the bst contains a name already in bts
        duplicates.append(name) # add the duplicate to duplicates

# Replace the nested for loops below with your improvements
# for name_1 in names_1: 0(n^2) nested for loops 7.707077264785767 seconds
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.