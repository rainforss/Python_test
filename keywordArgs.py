def myfunc(*args, **kwargs):
    print("I would like {} {}".format(args[0], kwargs["food"]))
    print(sum(args))


myfunc(1, 2, 3, food="watermelon", animal="ape")


def alternate(string):
    counter = 0
    modified = []
    for letter in string:
        if counter % 2 == 0:
            modified.append(letter.upper())
        else:
            modified.append(letter.lower())
        counter = counter + 1
    return "".join(modified)


print(alternate("ape"))

