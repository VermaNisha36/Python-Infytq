#Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers. 
#Note: Assume that all the numbers are two digit numbers.
#Sample Input:23,34,55
#Expected Output:553423

#PROGRAM

def create_largest_number(number_list):
    a=[]
    x=''
    for i in range(len(number_list)):
        m=max(number_list)
        a.append(m)
        number_list.remove(m)
    for i in range(len(a)):
        x=x+str(a[i])
    x=int(x)
    return x
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)