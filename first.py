#!usr/bin/python

n=int(raw_input("Enter the no. of elements :"))
a=[]
d=n
b=0
print "Enter the elements :"
for i in xrange(n):
    x=int(input())
    a.append(x)
for i in xrange(n):
    for j in range(i+1,n):
        if a[i]==a[j]:
            c=j-i
            if c<d:
               b=a[i]
               d=c
if not b:
    print "unique"
else:
    print b
