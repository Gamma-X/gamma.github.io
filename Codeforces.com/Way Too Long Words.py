l=[]
for i in range(int(input())):
    w=input()
    l.append(w)
for j in range(len(l)):
    if len(l[j])>10:
        print(l[j][0]+str(len(l[j])-2)+l[j][len(l[j])-1])
    else:
        print(l[j])
        
               
