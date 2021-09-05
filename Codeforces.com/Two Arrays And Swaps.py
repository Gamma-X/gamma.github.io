for _ in range(int(input())):
    n,k=input().split()
    a=[int(i)for i in input().split()]
    b=[int(i)for i in input().split()]
    a.sort()
    b.sort(reverse=True)
    c,x=0,0
    
    for i in range(len(a)):
        if i<=int(k)-1 and b[i]> a[i]:
            x=x+1
            c=c+int(b[i])
        if i>x-1:
            c=c+int(a[i])
    print(c)
            

    
