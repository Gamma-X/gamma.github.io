room=0
for _ in range(int(input())):
    p,q=input().split()   # p people living in it
                          # room can accommodate q people in total 
    if int(q)-int(p)>=2:
        room=room+1
print(room)

