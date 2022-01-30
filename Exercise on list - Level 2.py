#Exercise on list - Level 2
#Given a list of integer values. Write a python program to check whether it contains same number in adjacent position. Display the count of such adjacent occurrences
#Sample Input: [1,1,5,100,-20,-20,6,0,0]
#Expected Output: 3

#PROGRAM

def get_count(num_list):
    count=0

    # Write your logic here
    for i in range(len(num_list)-1):
        if num_list[i]==num_list[i+1]:
            count+=1
    return count

#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))