for _ in range(int(input())):
    n=int(input())
    num=[int(i)for i in list(input())]
    
    num1=[]
    num2=[]
    if n%2==0:   
        for i in range(1,n,2):
            
            num1.append(num[i])
        
        for k in  range(len(num1)):
            if num1[k]%2!=0:
                num1[k]='.'
        
        if all([a=='.'for i in num1]):
            print('1')
        else:
            print('2')
            
    else:
        for j in range(0,n,2):
            num2.append(num[j])
          
        for j in  range(len(num2)):
            if num1[j]%2==0:
                num2[j]='.'
        
        if all([a=='.'for i in num2]):
            print('2')
        else:
            print('1')
    
         



