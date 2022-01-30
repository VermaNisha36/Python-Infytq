#Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.
#Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.
#Sample Input: "I like Python"
#              "Java is a very popular language"
#Expected output: lieyon

#PROGRAM

def find_common_characters(msg1,msg2):
    common=''
    fact=0
    for i in msg1:
        for j in msg2:
            if i==j and i!=" ":
                if i not in common:
                    common=common+i
                    fact=1
                    break
    if fact==0:
        return -1
    else:
        return common
    #Remove pass and write your logic here

#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
