#Write a python function find_smallest_number() which accepts a number n and returns the smallest number having n divisors.
#Handle the possible errors in the code written inside the function.
#Sample Input: 16
#Expected Output: 120

#PROGRAM

def find_smallest_number(num):
    x=1
    while True:
        count=0
        for i in range(1,x+1):
            if x%i==0:
                count+=1
        if count==num:
            return x
        x+=1
num=18
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
