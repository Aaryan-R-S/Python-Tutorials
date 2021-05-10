f = open('27.txt')

try:
    open('dcacf.txt')
except Exception as e:
    print('[ERROR HAI BHAI]', e)
else:
    print('Either [except] or [else] shall be printed')
finally:
    f.close()
    print("Run this Anyway!")  # used for code cleanup like closing opened files

print('This is important!')