#Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.
#Write a python function which performs the run length encoding for a given String and returns the run length encoded String.
#Provide different String values and test your program
#Sample Input: AAAABBBBCCCCCCCC
#Expected Output: 4A4B8C

#PROGRAM

def encode(message):
    encoded_message = ""
    i = 0
   
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j+1]):
                count = count+1
                j = j+1
            else:
                break
        encoded_message=encoded_message+str(count)+ch
        i = j+1
    return encoded_message

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)