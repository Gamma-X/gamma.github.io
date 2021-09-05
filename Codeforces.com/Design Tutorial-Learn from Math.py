def compo(c):
    '''it will whether the number is composite or not.'''
    for i in range(2,c):
        if c%i==0:
            return(True)
            break
        else:
            return(False)

n=int(input())
f=n//2
s=n//2
if n%2!=0:
    f=f+1
    

while True:
    if compo(f):
        if compo(s):
            print(f,' ',s,sep='')
            break
        else:
            f=f+1
            s=s-1
    else:
        f=f+1
        s=s-1



   

       

    


    
