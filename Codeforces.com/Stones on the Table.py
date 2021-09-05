input()
s=input()
c=0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        continue
    else:
        c=c+1
print(c)
