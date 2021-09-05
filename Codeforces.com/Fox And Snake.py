n,m=input().split()
n=int(n);m=int(m)

sk=['#'*m,'.'*(m-1)+'#','#'*m,'#'+'.'*(m-1)]
j=0
for i in range(1,n+1):
    print(sk[j])
    j=j+1
    if j==4:
        j=0
