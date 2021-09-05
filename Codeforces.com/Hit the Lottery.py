n=int(input())
dollor=[100,20,10,5,1]
minm=0
i=0

while i<len(dollor):
    if n//dollor[i]!=0:
        minm=minm+n//dollor[i]
        n=n%dollor[i]
        
    else:
        i=i+1
print(minm)
    
