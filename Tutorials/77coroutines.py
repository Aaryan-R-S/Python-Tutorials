print('Wait...')

def search():
    import time
    # some 4 sec consuming task 
    book = "ant bat cat dog eagle fowl goat horse"
    time.sleep(4)

    while True:
        text = (yield)   # make couroutine
        if text in book :
            print('Yes')
        else :
            print('No')


s = search()

next(s)    # calling func

s.send(input('Type\n '))    # next time it will run from While -- so no time delay
s.send(input('Type\n '))
s.send(input('Type\n '))

s.close()