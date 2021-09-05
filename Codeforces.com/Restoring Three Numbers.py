num=[int(i)for i in input().split()]

abc=max(num)
num.remove(max(num))

a=abc-num[0]
b=abc-num[1]
c=abc-num[2]

print(a,b,c,sep=' ')
