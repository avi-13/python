# Write a Python program to count the number of strings 
# where the string length is 2 or more and 
# the first and last character are same from a given list of strings.
l = ['dfd','k','5' "ffsd","hggsdfh"]
count = 0
for i in l :
    if len(l)>2:
        if i[0]==i [len(i)-1]:
            count +=1
print (count)