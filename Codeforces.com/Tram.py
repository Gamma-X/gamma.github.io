trm=0
cap=[]
for _ in range(int(input())):
    ins,outs=list(map(int,input().split()))
    trm=trm-ins
    trm=trm+outs
    cap.append(trm)
print(max(cap))    
    
