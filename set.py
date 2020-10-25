# Sets are unordered collections of unique elements

my_set = set()

my_set.add(1)

my_set.add(2)

# Adding repeated value, only one appears
my_set.add(2)
print(my_set)

# Initiate a set with a list
my_list=[3,2,2,3,1]
my_set = set(my_list)
print(my_set)