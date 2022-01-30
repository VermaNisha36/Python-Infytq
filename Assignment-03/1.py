#Write a Python program to generate the next 15 leap years starting from a given year.
#Populate the leap years into a list and display the list. 

#PROGRAM

def find_leap_years(given_year):
    list_of_leap_years=[]
    count=0
    # Write your logic here
    
    i=0
    while(count<15):
        year=given_year+i
        if ((year%4==0) and (year%100!=0)) or (year%400==0):
            list_of_leap_years.append(year)
            count+=1
        i=i+1
    return list_of_leap_years

list_of_leap_years=find_leap_years(1784)
print(list_of_leap_years)