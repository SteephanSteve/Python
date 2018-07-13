#!usr/bin/python

n=int(input("N :"))
m=int(input("M :"))
a=[]
b=[]
c=0
print "A :"
for i in range(n):
      x=int(input())
      a.append(x)
print "B :"      
for i in range(m):
      x=int(input())
      b.append(x)
if n>m:
   for i in range(m):
       if b[i] not in a:
          c+=1
if c==0:
   print "YES"
else:
   print "NO"
