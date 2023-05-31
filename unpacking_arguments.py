
def multiply(*args):
    print(args)
    total=1
    for arg in args:
        total=total*arg
    return total

multiply(1,2,3)