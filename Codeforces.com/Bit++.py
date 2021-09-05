bit=0
for i in range(int(input())):
    b=input()
    
    for j in range(len(b)):
        if b[j]=='+':
            bit=bit+1/2
        if b[j]=='X':
            bit=bit+0
        if b[j]=='-':
            bit=bit-1/2

print(int(bit))
