#!usr/bin/python

n=int(raw_input("Enter the no. of elements :"))
a=[]
print "Enter the elements :"
for i in xrange(n):
    x=int(input())
    a.append(x)
for i in xrange(n):
    for j in xrange(n):
        for k in xrange(n):
            if a[i]+a[j]==a[k] and i<j<k:
                print a[i],a[j],a[k]
        
