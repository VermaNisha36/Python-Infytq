#Write a python function, find_pairs_of_numbers() which accepts a list of positive integers with no repetitions and returns count of pairs of numbers in the list that adds up to n. 
#The function should return 0, if no such pairs are found in the list.
#Sample Input: [1, 2, 7, 4, 5, 6, 0, 3], 6
#Expected Output: 3

#PROGRAM

def find_pairs_of_numbers(num_list,n):
    count=0
    l=set(num_list)
    for i in l:
        for j in l:
            if i!=j and int(i)+int(j)==int(n):
                count+=1
    count=count//2
    return count
    #Remove pass and write your logic here

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))
