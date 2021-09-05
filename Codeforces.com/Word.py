wrd=input()

u,l=0,0
for i in wrd:
    if i.isupper():
        u=u+1
    else:
        l=l+1
if u>l:
    print(wrd.upper())
else:
    print(wrd.lower())
        
        
