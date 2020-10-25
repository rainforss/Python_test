# Key value pairs which are similar to javascript objects, no order, hashed table structure

my_dict = {'apple':3,'watermelon':"expensive",'priceList':[2,5,6,1],'nested':{'insideKey':[100,200]}}

# Key value pair lookup
print(my_dict['nested']['insideKey'])

# Chained operators
my_dict['nested']['insideKey'][0] = 211
print(my_dict['nested']['insideKey'])

# Pass by value, the new variable is assigned a copy of the dictionary in memory, mutating the new variable does not change the original dictionary
new_num = my_dict['nested']
print(new_num)
new_num = 999
print(my_dict['nested'])
print(new_num)

# Get keys or values or items
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())



