me = 'ARS'
gt = 'Hi!'

a = 'This is %s %s' %(me, gt)
print(a)

#   --OR--

me = 'ARS'
gt = 'Hi!'

a = 'This is {} {}'
a = 'This is {1} {0}'
b = a.format(me, gt)
print(b)

#   --OR--

import math

me = 'ARS'
gt = 'Hi!'

a = f'This is {me} {gt} {math.cos(math.pi*2)}'
print(a)

