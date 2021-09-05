input()
fd_indx=[]
f=''
fd=input().split(' ')

[fd_indx.append([int(fd[i-1]),i])for i in range(1,len(fd)+1)]
fd_indx.sort()

for i in range(len(fd_indx)):
    f=f+str(fd_indx[i][1])
    f=f+' '
    
print(f)
