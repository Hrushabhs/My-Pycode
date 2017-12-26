
for n in range(3,100):
    for m in range(2,n):
        if n%m==0:
            j=n/m
            print "%d = %d * %d " %(n,m,j)
            break
        else:
            print n," The number is Prime Number"
            break