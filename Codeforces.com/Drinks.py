n=int(input())
vol_p=0

vol_frac=[int(i)for i in input().split()]
for i in range(len(vol_frac)):
    vol_p=vol_p+vol_frac[i]*1/100
print((vol_p/n)*100)
