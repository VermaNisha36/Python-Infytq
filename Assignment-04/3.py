#Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
#The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.
#The function should identify the degree of correctness as mentioned below:
#CORRECT, if it is an exact match
#ALMOST CORRECT, if no more than 2 letters are wrong
#WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.
#and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
#Assume that the words contain only uppercase letters and the maximum word length is 10.
#Sample Input: {"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
#Expected Output: [2, 2, 1]

#PROGRAM

def find_correct(word_dict):
    #start writing your code here
    list=[]
    correct=0
    almost_correct=0
    incorrect=0
    x=len(word_dict)
    y=[]
    z=[]
    for key,value in word_dict.items():
        y.append(key)
        z.append(value)
    for i in range(x):
        if y[i]==z[i]:
            correct+=1
        else:
            if len(y[i])==len(z[i]):
                a=len(y[i])
                b=y[i]
                c=z[i]
                m=0
                for j in range(a):
                    if b[j]!=c[j]:
                        m+=1
                    j+=1
                if m<=2 and m>0:
                    almost_correct+=1
                else:
                    incorrect+=1
            else:
                incorrect+=1
        i+=1
    list.append(correct)
    list.append(almost_correct)
    list.append(incorrect)
    return list
    
word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))