#!usr/bin/python

n=input()
k=input()
l=list(str(n))
for i in range(k):
    del l[0]
print ''.join(l)
    
        
