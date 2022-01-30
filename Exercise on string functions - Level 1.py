#Exercise on string functions - Level 1
#Write a python program which displays the count of the names that matches a given pattern from a list of names provided.
#Consider the pattern characters to be:
#1. "_ at" where "_" can be one occurrence of any character
#2. "%at%" where "%" can have zero or any number of occurrences of a character
#Sample Input: [Hat, Cat, Rabbit, Matter]
#Expected Output: _at -> 2
#                 %at% -> 3

#PROGRAM

def count_names(name_list):
    count1=0
    count2=0
    
    #start writing your code here
    #Populate the variables: count1 and count2
    for name in name_list:
        if len(name)==3 and name.endswith("at"):
            count1+=1
        if len(name)>=2 and name.find("at")>=0 and name.find("at")<=len(name):
            count2+=1
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print("_at -> ",count1)
    print("%at% -> ",count2)


#Provide different names in the list and test your program
name_list=["Hat","Cat","rabbit","matter"]
count_names(name_list)