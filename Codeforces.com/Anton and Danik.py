input() #  no. of chess game played.
s=input()
A=len(''.join(s.split('D')))
D=len(''.join(s.split('A')))
if A>D:             
    print("Anton")  # Anton won more games than Danik.
if D>A:
    print( "Danik" ) # Danik won more games than Anton.
if A==D:
    print("Friendship") # Anton and Danik won the same number of games.
