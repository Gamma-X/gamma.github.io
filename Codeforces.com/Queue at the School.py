t=[int(i)for i in input().split()]
strg=input() #string

while t[1]>0:

    strg=strg.split('BG') #Swaping string with known string only
    strg='GB'.join(strg)
    
    t[1]=t[1]-1 #time 
print(strg)
    
