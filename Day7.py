# Sorting a List of Strings

my_list = ["Bananas", "Oranges", "Grapes", "Cherries"]

# Brute force Method using bubble sort
my_list = ["Bananas", "Oranges", "Grapes", "Cherries"]
size = len(my_list)
for i in range(size):
    for j in range(size):
        if my_list[i] < my_list[j]:
            temp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = temp

# Generic List sort *fastest*
my_list.sort()

# Casefold list sort
my_list.sort(key=str.casefold)

# Generic list sorted
my_list = sorted(my_list)

# Custom list sort using casefold
my_list = sorted(my_list, key=str.casefold)

# Custom list using current locale
from functools import cmp_to_key
import locale
my_list = sorted(my_list, key=cmp_to_key(locale.strcoll))

# Custom reverse list sort using casefold
my_list = sorted(my_list, key=str.casefold, reverse=True)
