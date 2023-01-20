import re



def DateCheck(day, month, year):
    #declaring variable valid
    valid = False
    #checking if leap year or not
    even_year = False

    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
        even_year = True

    if (month in [4, 6, 9, 11]) and (1<=day<=30):
        valid = True
    elif (month == 2) and (1<=day<=29) and even_year == True:
        valid = True
    elif (month == 2) and (1<=day<=28) and even_year == False:
        valid = True
    elif (month in [1, 3, 5, 7, 8, 10, 12]) and (1<=day<=31):
        valid = True

    if valid == True:
        print('Valid year')
    else:
        print('Invalid year')

date = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')

mo = date.search("Lets play basketball on 31/02/2020")

day = int(mo.groups()[0])   
month = int(mo.groups()[1])
year = int(mo.groups()[2])

DateCheck(day, month, year)

