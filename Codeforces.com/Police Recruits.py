input()
s=[int(i)for i in input().split()]
p=0 # police
c=0 # crimes
for i in range(len(s)):
    if s[i]==-1:
        if p!=0:
            p=p+s[i]
        else:
            c=c+s[i]
    else:
        p=p+s[i]

print(abs(c))
            
    
