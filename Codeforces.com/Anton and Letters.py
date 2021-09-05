sets=input()
lists=[]

for i in range(len(sets)):
    if sets[i] not in lists and sets[i]!='{' and sets[i]!='}' and sets[i]!=','and sets[i]!=' ':
        lists.append(sets[i])
print(len(lists))
