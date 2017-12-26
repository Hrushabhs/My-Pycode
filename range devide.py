lower=int(input("Enter lower range limit: "))
upper=int(input("Enter upper range limit:"))
n=int(input("Enter Number to be divided by: "))
for i in range(lower,upper+1):
    if(i%n==0):
        print i
    
