def function():
    '''give sum of n number with alternate opp.  sign.'''
    n=int(input())
    
    if n%2==0:
        e_o=n//2 # n is even.
    else:
        e_o=(n+1)//2  # n is odd

    sum_=((-1)**n)*e_o
    return sum_

print(function())    
