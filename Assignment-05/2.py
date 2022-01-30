#Consider sample data as follows: sample_data=range(1,11)
#Create two functions: odd() and even()
#The function even() returns a list of all the even numbers from sample_data
#The function odd() returns a list of all the odd numbers from sample_data
#Create a function sum_of_numbers() which will accept the sample data and/or a function.
#If a function is not passed, the sum_of_numbers() should return the sum of all the numbers from sample_data
#If a function is passed, the sum_of_numbers() should return the sum of numbers returned from the function passed.

#PROGRAM

def sum_of_numbers(list_of_num,filter_func=None):
    sum=0
    if filter_func==None:
        for i in list_of_num:
            sum+=i
        return sum
    elif filter_func==odd:
        l=odd(list_of_num)
        for j in l:
            sum+=j
        return sum
    else:
        l=even(list_of_num)
        for j in l:
            sum+=j
        return sum
        
def even(data):
    even_list =list()
    for i in data:
        if i % 2 == 0:
            even_list.append(i)
    return even_list
    

def odd(data):
    odd_list =list()
    for i in data:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list
    #Remove pass and write the logic here

sample_data = range(1,11)

print(sum_of_numbers(sample_data,odd(sample_data)))