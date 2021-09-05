p,t=input().split()
p=int(p);t=int(t)

min_t=240-t
sum_p=(5*p)*(1+p)/2

while sum_p>min_t:
    p=p-1
    sum_p=(5*p)*(1+p)/2

print(p)
    
