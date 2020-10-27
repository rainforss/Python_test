# Similar to list, but immutable, ensures data integrity

my_tuple = (1,2,3,3,5,2,'aString',{'key1':"value1","key2":"value2"})
my_list = [1,2,3]
another_tuple = (1,2,3)
print(my_tuple)
print(type(my_list),type(my_tuple))


# Count method returns the number of appearances of the input

print(my_tuple.count(1))
print(len(my_tuple))
print(sum(another_tuple))

# Index method returns the index of the first occurence of the input
print(my_tuple.index(3))