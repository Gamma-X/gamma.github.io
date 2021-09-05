# I have played this game but can't clear.

num_levels=int(input())
x=input().split()   # x_can_pass_levels
y=input().split()   # y_can_pass_levels
x.remove(x[0])
y.remove(y[0])
both=x+y
l=[]                # both_can_pass_levels 
for i in range(len(both)):
    if both[i] not in l and both[i]!='0':
        l.append(both[i])           
        
if  len(l)==num_levels:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
    
