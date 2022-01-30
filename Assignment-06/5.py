#A 10-substring of a number is a substring of its digits that sum up to 10.
#For example, the 10-substrings of the number 3523014 are:  3523014, 3523014, 3523014, 3523014
#Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 10-substrings of that string.
#Handle the possible errors in the code written inside the function.
#Sample Input: '3523014'
#Expected Output: ['5230', '23014', '523', '352']

#PROGRAM

def find_ten_substring(num_str):
    num_str=str(num_str)
    number=list(map(int,num_str))
    l=[]
    for i in range(len(num_str)):
        x=''
        Sum=0
        for j in range(i,len(num_str)):
            x+=str(num_str[j])
            Sum+=int(num_str[j])
            if Sum==10:
                l.append(x)
    return l
    #Remove pass and write your logic here

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)