#!usr/bin/python

x=raw_input("X :")
y=raw_input("y :")
a=abs(len(x)-len(y))
n=len(min(x,y))
x=list(x)
y=list(y)
for i in xrange(n):
    if x[i]!=y[i]:
        a+=1
print a
