def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,2,4,name="bob",age=25)