# def add(*args):
#     print(args)
#     return sum(args)

# print(add(1,2,2))


def add(*args):
    print(args)
    for i in args:
        print(i)
    return sum(args)

print(add(1,2,2))
# print(add('a','v')) # unsupported type
# var1 = add(1,2,3,4)



# def add(*args):
#     return sum(args)

# var1 = add(1,2,3,4)
# var2 = add(1,2,3,4,0,-1.-4)
# var3 = add(1,2,3,4,8,7,7,7)
# print(var1)
# print(var2)
# print(var3)