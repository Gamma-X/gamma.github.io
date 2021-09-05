for _ in range(int(input())):
    a,b=[int(i)for i in  input().split()]
    x=max(a,b);y=min(a,b)
    
    if y*2>x:
        area=(y*2)**2
    else:
        area=(x)**2

    print(area)
