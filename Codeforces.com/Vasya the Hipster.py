RB=[int(i)for i in input().split()] # red,blue.

diff=min(RB)            # different socks.
same=(max(RB)-diff)//2  # same socks.

print(diff,' ',same,sep='') 
