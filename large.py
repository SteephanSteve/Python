#!usr/bin/python

n=raw_input("Enter the no. of elements :")
a=[]
print "Enter the elements :"
for i in xrange(int(n)):
    x=int(input())
    a.append(x)
a.sort(reverse=True)
b=int(''.join(map(str,a)))
print b
