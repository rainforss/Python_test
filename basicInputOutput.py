myFile = open('myfile.txt')


# Throws FileNotFoundError
# wrongFile = open('foobar.text')


# Return the whole text as a string, need to reset the cursor if read a second time
print(myFile.read())
print(myFile.read()) # Outputs none
myFile.seek(0)
print(myFile.read())

# Return lines in a list
myFile.seek(0)
print(myFile.readlines())
myFile.seek(0)

myFile.close()

with open('myfile.txt') as my_file:
    contents = my_file.readlines()
    print(contents)

# Write mode will create new file if no existent
with open('foobar.txt',mode="w") as f:
    f.write('Foo Bar')

# Read mode does not allow write operations
with open('foobar.txt',mode="r") as f:
    # f.write('Ape') throws error 
    print(f.read())