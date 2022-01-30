#Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
#Words at odd position -> Reverse It
#Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change
#Note: Assume that the sentence would begin with a word and there will be only a single space between the words.
#Perform case sensitive string operations wherever necessary.
#Sample Input: the sun rises in the east
#Expected Output: the sun rises in the east

#PROGRAM

def encrypt_sentence(sentence):
    x=sentence.split()
    new_sentence=[]
    answer=''
    for i in range(1,len(x)+1):
        message=x[i-1]
        if i%2==0:
            result=''
            consonant=''
            vowel=''
            for j in range(len(message)):
                if message[j]=='a' or message[j]=='e' or message[j]=='i' or message[j]=='o' or message[j]=='u':
                    vowel=vowel+message[j]
                else:
                    consonant+=message[j]
                j+=1
            result=consonant+vowel
            new_sentence.append(result)
        else:
            reverse=''
            for j in range(len(message)-1,-1,-1):
                reverse=reverse+message[j]
            new_sentence.append(reverse)
        i+=1
    for k in new_sentence:
        if k==new_sentence[0]:
            answer=answer+k
        else:
            answer=answer+" "+k
    return answer
    #start writing your code here

sentence="The sun "
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
