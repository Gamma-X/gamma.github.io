x=int(input()) #point where  elephant had to go.
rem=x%5
ques=x//5

if rem==0:
    print(ques) #minim no. of steps.
else:
    print(ques+1)
