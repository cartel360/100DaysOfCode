# Converting Two List into a Dictionary

column_names = ['id', 'Name', 'Reg_No']
column_values = [1, 'Billy', 'BIT/001']

# Converting with the zip and dict constructor
converted_dict = dict(zip(column_names, column_values))

# Converting using dictionary compression
converted_dict1 = {key: value for key,
                   value in zip(column_names, column_values)}

# Converting with a loop
names_values_tuple = zip(column_names, column_values)
converted_dict2 = {}
for key, value in names_values_tuple:
    if key in converted_dict2:
        pass
    else:
        converted_dict2[key] = value

print(converted_dict)
print(converted_dict1)
print(converted_dict2)
