#!usr/bin/python

n=int(raw_input("Enter the no. of elements :"))
a=[]
d=n
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
print b
