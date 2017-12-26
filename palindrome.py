n=int(input("Enetr number: "))
t=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(t==rev):
    print"The Given number is palidrome"
else:
    print"The given number is not palidrome"

