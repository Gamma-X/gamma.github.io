input()
wel_citz=[int(i)for i in input().split()]

a=0
for j in range(len(wel_citz)):

    a=a+(max(wel_citz)-wel_citz[j])

print(a)
