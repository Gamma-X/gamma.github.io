for _ in range(int(input())):
    s=input()
    sr=[]
    for i in range(3,len(s),2):
        sr.append(s[i])
    print(s[0]+s[1]+''.join(sr))
