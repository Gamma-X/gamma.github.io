x=[int(i)for i in  input().split()]

co1=max(x);x.remove(co1) # max coordinate. 
co2=min(x);x.remove(co2) # min coordinate.
meet=0

meet=meet+(x[0]-co2)
meet=meet+(co1-x[0])

print(meet)
