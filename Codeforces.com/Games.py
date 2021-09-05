match=[]
for _ in range(int(input())):
    hg=input().split()   # host,guest
    match.append(hg)

uniform=0
for j in range(len(match)):

    for i in range(len(match)):
        if match[j][0]==match[i][1]:
            uniform=uniform+1

print(uniform)
