# Cloning a List

import copy
my_list = [30, 25, 65, 45, 47]

# Clone a List by Bruteforce
duplicate_list = [item for item in my_list]

# Clone a List by Slice
duplicate_list1 = my_list[:]

# Clone a List with List Constructor
duplicate_list2 = list(my_list)

# Clone a List with Copy Function
duplicate_list3 = my_list.copy()

# Clone a list with Copy Package
duplicate_list4 = copy.copy(my_list)
deep_duplicate_list4 = copy.deepcopy(my_list)

# Clone a List with Multiplication
duplicate_list5 = my_list * 1  # Never advisable
