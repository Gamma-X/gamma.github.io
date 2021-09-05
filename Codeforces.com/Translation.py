ber=input() # Berlandish word
bir=input() # Birlandish word

for i in range(len(ber)):
    if ber[i]==bir[-(i+1)]:
        c=i
    else:
        print('NO')
        break
    if c==len(ber)-1:
        print('YES')
        
        
        
        
