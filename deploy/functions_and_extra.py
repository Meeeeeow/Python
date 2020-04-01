# functions
# args and kwargs
a = 0  # global scope or variable


def addition(*args, **kwargs):
    '''
    a function to demonstrate args and keyword agrs
    '''
    # * dea thkle it can take multiple number of arguments
    print(*args)  # 1 2
    print(args)  # (1,2)
    print(kwargs)  # {'name1': 's', 'name2': 'a'}
    total = ''
    for items in kwargs.values():
        total += items
    print(total)  # sa (concat korlm)
    return str(sum(args)) + total


print(addition(1, 2, 3, 10, name1='s', name2='a'))
help(addition)
print(addition.__doc__)
# Exercise
temp = 0  # global
highes_value = 0  # global


def highest_even(li):
    evens = []
    for item in li:
        if (item % 2 == 0):
            evens.append(item)
    highest_value = evens[0]
    # print(highest_value)
    for items in evens:
        # print(items)
        if (items > highest_value):
            highest_value = items

    return highest_value
    # or return max(evens)1st method


print(highest_even([10, 2, 3, 4, 8, 11, 12]))
# scope theke mainly name error ashe

# global but not too good to Use
tot = 0


def counter():
    # not too good to use
    global tot
    tot += 1
    return tot


counter()
counter()
print(counter())


# better use
def counter1(tot):  # tot = 3
    tot += 1
    return tot


print(counter1(counter1(counter1(tot))))
# local and non locals
a = 2


def outer():
    x = 6
    print(a)

    def inner():
        # nonlocal x
        x = 5 + a
        print(x)

    inner()
    print(x)


outer()    