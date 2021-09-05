for _ in range(int(input())):
    n=int(input())
    b,a=0,0
    b=b+2**n
    for i in range(1,n):
        if i<n//2:
            b=b+2**i
        if i>=n//2:
            a=a+2**i

    minm_diff=b-a
    print(minm_diff)
