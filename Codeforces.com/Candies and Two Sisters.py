for _ in range(int(input())):
    num_cand=int(input())

    if num_cand%2==0:
        num_ways=(num_cand-2)//2
    else:
        num_ways=(num_cand-1)//2
    print(num_ways)
