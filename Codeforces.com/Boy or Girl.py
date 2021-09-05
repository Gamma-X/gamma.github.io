n=input()
l=[]
for i in range(len(n)):
    if n[i] not in l:
        l.append(n[i])
if len(l)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
        
    
