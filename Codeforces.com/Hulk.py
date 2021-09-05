feel=''
layer=int(input())

for i in range(1,layer+1):
    if i%2!=0:
        feel=feel+'I hate'
    else:
        feel=feel+'I love'
    if i==layer:
       feel=feel+' it'
       break
    else:
        feel=feel+' that '
        
print(feel)        
