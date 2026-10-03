a = 10
b = 9
c = 8


def something():
    a = 4
    x = globals()['a']
    print("id of x is : {} and a is : {} and x is : {} ".format(id(x), a, x))


something()
print(a)
