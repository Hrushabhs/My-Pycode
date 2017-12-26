n=int(input("Enetr number: "))
count=0
while(n>0):
    dig=n%10
    count+=1
    n=n/10
print count
