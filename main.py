import random
z,p,r=0,0,100
a=[random.randint(-200,200) for i in range(r)]
print(*a)
for i in range(r):
    if a[i]==0: z+=1
    elif a[i]>0: p+=1
print("max=",max(a),"  mix=",min(a))
print ("0=",z,"positive=",p,"negative=",r-p-z)