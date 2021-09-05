k,n,w=list(map(int,input().split()))
t=0
for i in range(1,w+1):
    t=t+(k*i)
if  t>n:
    print(t-n)
else:
    print('0')
