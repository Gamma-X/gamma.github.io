row=[]
col=[]
ck=0
for i in range(5):
    elm=input().split()
    row.append(elm)
for i in range(len(row)):
    col.append([row[j][i]for j in range(len(row[i]))])
for i in range(len(row)):
    for j in range(len(row[i])):
        if row[i][j]!='0':
            ck=ck+abs(2-i)
for i in range(len(col)):
    for j in range(len(col[i])):
        if col[i][j]!='0':
            ck=ck+abs(2-i)
print(ck)
        
        
                                                           
