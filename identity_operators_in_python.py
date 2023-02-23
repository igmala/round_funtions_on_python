a = 5
b = 5
c = 4
d = '5'
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(a is b)
print(a is c)
print(a is not c)
print(b is not c)
print (a is not d)

a = 5
print(id(a))
a = 8
print(id(a))
print(a is a)