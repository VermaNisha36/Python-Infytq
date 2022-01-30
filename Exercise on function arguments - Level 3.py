#Exercise on function arguments - Level 3
#Write a Python function to find all the Strong numbers in a given list of numbers.
#Write another function to find and return the factorial of a number. Use it to solve the problem.
#Example:A number is considered to be a Strong number if sum of the factorial of its digits is equal to the number itself. 
##145 is a Strong number as 1! + 4! + 5! = 145. 
#Sample Input: num_list = [145,375,0,100,2]
#Expected Output: [145, 2]

#PROGRAM

def factorial(number):
     if number==0:
         return 1
     else:
         result=1
         for i in range(1,number+1):
            result=result*i
         return result
     #remove pass and write your logic to find and return the factorial of given number


def find_strong_numbers(num_list):
    list=[]
    for i in num_list:
      if i!=0:
         num=i
         sum=0
         while(num!=0):
             rem=num%10
             sum=sum+factorial(rem)
             num=num//10
         if i==sum:
             list.append(i)
    return list
    #remove pass and write your logic to find and return the list of strong numbers from the given list


num_list=[145, 375, 100, 2, 10, 40585, 0]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)