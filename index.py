#!usr/bin/python

n=int(raw_input("Enter the no. of elements :"))
a=[]
b=[]
print "Enter the elements :"
for i in xrange(n):
    x=int(input())
    a.append(x)
for i in xrange(n):
    if i==a[i]:
        b.append(i)
if len(b)==0:
    print "-1"
else:
    print b
     
