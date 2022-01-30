#Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence. 
#Rules are as follows: 
#a. Spaces are to be retained as is 
#b. Each word should be encoded separately
#If a word has only vowels then retain the word as is
#If a word has a consonant (at least 1) then retain only those consonants
#Note: Assume that the sentence would begin with a word and there will be only a single space between the words.
#Sample Input: I love Python
#Expected Output: I lv Pythn

#PROGRAM

def sms_encoding(data):
    #start writing your code here
    word=data.split()
    vowels="aeiouAEIOU"
    st=""
    for i in word:
        if(len(i)==1):
            st=st+i
        else:
            for j in i:
                if j not in set(vowels):
                    st=st+j
        st=st+" "
    return st[0:-1]

data="I will not repeat mistakes"
print(sms_encoding(data))