guest=input()
host=input()
mixed=input()
unmixed=guest+host

x=''
u=[]
m=[]

[u.append(i)for i in unmixed]
[m.append(j)for j in mixed]

u.sort()
m.sort()
'''print(m)
print(u)'''
if len(u)!=len(m):
    print("NO")
else:
    for i in range(len(u)):
        if u[i]==m[i]:
            x=i
            continue
        else:
            print( "NO")
            break
    if x==len(u)-1:
        print("YES")
