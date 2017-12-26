year=int(input("Enetr number: "))
if(year%4==0 and year%100!=0 and year%400!=0):
    print"This year is leap Year"
else:
    print("This year is not leap year")
