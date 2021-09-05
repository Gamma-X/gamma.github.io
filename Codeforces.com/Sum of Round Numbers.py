for _ in range(int(input())):
    n=input()
    ro=''
    c=0
    for i in range(len(n)):
        if n[i]!='0':
            r=n[i]+('0'*(len(n)-(i+1)))
            ro=ro+r+' '
            c=c+1
    print(c)
    print(ro)
