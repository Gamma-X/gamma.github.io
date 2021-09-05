a=input()
b=input()
new=''
for i  in range(len(a)):
    if a[i]==b[i]:
       new=new+'0'
    else:
        new=new+'1'
print(new)
