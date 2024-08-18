x =99
def outer(num):
    def inner(x):
        return x**num
    return inner

s = outer(2)
c = outer(3)

print(s(4))
print(c(4))