hf=[int(i)for i in input().split()] # height of fence.
hp=input().split()  # height of person.

width=0

for i in hp:
    if int(i)>hf[1]:
        width=width+2
    else:
         width=width+1

print(width) # minimum width of road.
