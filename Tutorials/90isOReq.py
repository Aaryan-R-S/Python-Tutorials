# == : Value Equality [same value of two different objects]
# is : Reference Equality [two object refer to same third object]

a = [4,3,6]
b = a

print(b==a)  # True
print(b is a)  # True
print(a is b)  # True


a = [4,3,6]
b = [4,3,6]

print(b==a)  # True
print(b is a)  # False
print(a is b)  # False