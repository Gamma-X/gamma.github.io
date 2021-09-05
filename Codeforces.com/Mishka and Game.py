mis,ch=0,0

for _ in range(int(input())):
    m,c=input().split()
    m=int(m);c=int(c)
    
    if m>c:
        mis=mis+1
    if c>m:
        ch=ch+1
if mis>ch:
    print("Mishka")
if ch>mis:
    print("Chris")
if ch==mis:
    print("Friendship is magic!^^")
        
        
