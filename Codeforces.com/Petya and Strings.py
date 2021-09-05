s=input().lower()
c=input().lower()
for i in range(len(s)):
    if s[i]==c[i] and i==len(s)-1:
        print('0')
        break
    if s[i]==c[i]:
        continue
    
    elif ord(s[i])>ord(c[i]):
        print('1')
        break
    else:
        print('-1')
        break

        
