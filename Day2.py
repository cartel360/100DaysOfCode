from collections import defaultdict
my_dict = {
    "Name": "Billy Dan",
    "Tool": "Python",
    "Alias": "Anonymous",
    "Phone": "+254 799 092010",
    "Langauge": "Python"
}

# Use to invert dictionaries that have unique values
my_inverted_dict = dict(map(reversed, my_dict.items()))

# Use to invert dictionaries that have unique Values
my_inverted_dict = {value: key for key, value in my_dict.items()}

# Use to invert dictionaries that have non-unique values
my_inverted_dict = defaultdict(list)
{my_inverted_dict[v].append(k) for k, v in my_dict.items()}

# Use to invert dictionaries that have non-unique values
my_inverted_dict = dict()
for key, value in my_dict.items():
    my_inverted_dict.setdefault(value, list()).append(key)

# Use to invert dictionaries that have lists of values
my_dict = {
    value: key for key in my_inverted_dict for value in my_inverted_dict[key]}

print(my_dict)
print(my_inverted_dict)