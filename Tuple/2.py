# Write a Python program to convert a tuple to a string.

def convertTuple(tup):
		# initialize an empty string
	str = ''
	for item in tup:
		str = str + item
	return str


# Driver code
tuple = ('h', 'e', 'l', 'l', 'o','w','o','r','l','d')
str = convertTuple(tuple)
print(str)
