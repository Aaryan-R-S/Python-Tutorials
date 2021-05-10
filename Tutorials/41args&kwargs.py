n = 'YO! '
x = ['HTML', 'CSS', 'JS', 'NodeJS', 'MongoDb', 'PYTHON']
z = {'1':'edx', '2':'cdf', '3':'dcsvt'}

def f1(normal, *args, **kwargs):            # list goes as TUPLE in args

    print(normal)                 # normal argument then args then kwargs

    # print(args[0])
    #   --OR--
    for q in args:
        print(q)

    for e in kwargs:
        print(e, ':', kwargs[e])

    for e, a in kwargs.items():
        print(e,'-', a)

f1(n, *x, **z)
