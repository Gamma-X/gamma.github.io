n=int(input())
pangram=input().lower()
pangram=set(pangram)

if len(pangram)==26:
    print("YES")
else:
    print("NO")
