same_pole=''
grp=0
for _ in range(int(input())):
    mag=input()
    if mag==same_pole:
        continue
    else:
        grp=grp+1
        same_pole=mag
print(grp)

        
    
