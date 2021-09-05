for _ in range(int(input())):
    n=int(input())
    l=input().split()
    c=0
    for i in  range(len(l)-1):
        if l[i]=='1':
             c=c+1
        if l[i]!='1' and l[i]!='0':
            if n%2==0:
              if (i+1)%2==0:
                c=c+1
              else:
                  c=c+2
            else:
                if (i+1)%2!=0:
                    c=c+1
                else:
                    c=c+2
    if l[len(l)-1]!='0':
        c=c+1

    if c%2!=0:
        print("First")
    else:
        print("Second")
    
