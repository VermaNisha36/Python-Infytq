#Write a python function find_duplicates(), which accepts a list of numbers and returns another list containing all the duplicate values in the input list and the order should be same as in the input list. 
#If there are no duplicate values, it should return an empty list.
#Sample Input: [12,54,68,759,24,15,12,68,987,758,25,69]
#Expected Output : [12, 68]

#PROGRAM

def find_duplicates(list_of_numbers):
    l=[]
    for i in list_of_numbers:
        x=list_of_numbers.count(i)
        if x>=2:
            l.append(i)
    l=set(l)
    l=list(l)
    return l
    #start writing your code here

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)