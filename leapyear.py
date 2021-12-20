import datetime
date = datetime.date.today()
currentYear = int(date.strftime("%y"))
print("enter the last year")
endYear = int(input())
print("list of leap Year")
for year in range(currentYear,endYear):
    if((year%4==0)and(year%100!=0)or(year%40==0)):
        print(year)
