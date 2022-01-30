#Write a python function to check whether three given numbers can form the sides of a triangle. 
#Hint : Three numbers can be the sides of a triangle if none of the numbers are greater than or equal to the sum of the other two numbers.

#PROGRAM

def form_triangle(num1,num2,num3):
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    if num1+num2>num3 and num1+num3>num2 and num2+num3>num1:  #Triangle Property
        return success
    else:
        return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1=9
num2=2
num3=5
print(form_triangle(num1, num2, num3))