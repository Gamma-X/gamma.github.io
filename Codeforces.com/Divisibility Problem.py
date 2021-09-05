for _ in range(int(input())):
    a,b=input().split()
    a=int(a);b=int(b)

    rem=a%b

    if rem==0:
        min_moves=0
    else:
        min_moves=b-rem

    print(min_moves)
