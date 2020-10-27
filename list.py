print("hello world")
msg = "Hello world"
my_list = [5, 2, 3]
another_list = ["banana", "apple", "watermelon"]

# Concat
new_list = my_list + another_list
print(new_list)


# Append mutates the list by adding at the end of a list
my_list.append(7)

# Pop mutates the list by popping at the index of a list, default -1 at the end of the list
my_list.pop()

# Sort directly sorts the list which invokes the method without returning anything
my_list.sort()
another_list.sort()

# Reverse directly reverse the list which invokes the method without returning anything
my_list.reverse()

print(my_list)

