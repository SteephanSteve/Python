#!usr/bin/python

n=raw_input("Enter the no. of elements :")
a=[]
b=[]
print "Enter the elements :"
for i in xrange(int(n)):
    x=int(input())
    a.append(x)
for i in xrange(int(n)):
    for j in range(i+1,int(n)):
        if a[i]==a[j]:
            b.append(a[i])
if len(b)==0:
    print "Unique"
else:
    for i in xrange(len(b)):
     for j in range(i+1,len(b)):
        if b[i]>b[j]:
            b[i]=b[i]+b[j]
            b[j]=b[i]-b[j]
            b[i]=b[i]-b[j]
    print b
            
