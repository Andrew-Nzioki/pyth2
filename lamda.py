(lambda x,y:x+y)(5,6)

def double(x):
    return x*2

sequence=[1,3,5,9]
# doubled=[double(x) for x in sequence]

doubled=list(map(lambda x:x*2,sequence))