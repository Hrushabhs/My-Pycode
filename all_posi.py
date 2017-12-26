
a=int(input("Enter 1st value"))
b=int(input("Enter 2nd value"))
c=int(input("Enter 3rd value"))
f=int(input("Enter 4rd number"))
d=[]
d.append(a)
d.append(b)
d.append(c)
d.append(f)
for i in range(0,4):
    for j in range(0,4):
        for k in range(0,4):
            for l in range(0,4):
                if(i!=j&j!=k&k!=l&l!=i&l!=j&k!=i):
                    print(d[i],d[j],d[k],d[l])