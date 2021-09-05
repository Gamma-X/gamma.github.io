for _ in range(int(input())):
 
    n=int(input())
    la,lb=[],[]
    a,b=2,1

    if (n//2)%2!=0:
        print('NO')
    else:
         
        for i in range(n//2):
            la.append(a)
            a=a+2
            lb.append(b)
            b=b+2
     
        
        lb[(n//2)-1]=lb[(n//2)-1]+n//2
     
        c=''
        print('YES')
        for j in (la+lb):
            c=c+(str(j)+' ')
        print(c)
      
