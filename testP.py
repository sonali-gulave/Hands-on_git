def f(arg1,arg2,kwarg1="kw1",kwarg2='kw2',*args,**kwargs):
    print('arg:{0},arg2:{1}''kwarg1:{2},kwarg2:{3}'.format(arg1,arg2,kwarg1,kwarg2))
    if args:
        print('args: ',str(args))
    if kwargs:
        print('kwargs: ',kwargs)
