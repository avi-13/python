#  Write a Python program to remove an item from a set if it is present in the set.
a= {1,2,2,3,'hello','ok','python'}
print(a)
if 'hello' in a:
    a.remove('hello')
    print(a)
else:
    print("not present")