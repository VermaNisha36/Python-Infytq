#Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.
#The number and its double should have exactly the same number of digits.
#Both the numbers should have the same digits ,but in different order.
#Otherwise it should return False.
#Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.

#PROGRAM

def check_double(number):
    x= [int(a) for a in str(number)]
    number=int(number)
    double=int(number*2)
    y= [int(a) for a in str(double)]
    x=sorted(x)
    y=sorted(y)
    if len(x)==len(y) and x==y:
        return True
    else:
        return False
    #Remove pass and write your logic here

#Provide different values for number and test your program
print(check_double(125874))