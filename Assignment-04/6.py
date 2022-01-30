#Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.
#Rules:
#The word should have the largest frequency.
#In case multiple words have the same frequency, then choose the word that has the maximum length.
#Assumptions:
#The text has no special characters other than space.
#The text would begin with a word and there will be only a single space between the words.
#Perform case insensitive string comparisons wherever necessary.
#Sample Input: "Work like you do not need money love like you have never been hurt and dance like no one is watching"
#Expected Output: like 3

#PROGRAM

def max_frequency_word_counter(data):
    word=""
    frequency=0
    my_dic={}
    data_list=data.split()
    for x in data_list:
        value=data_list.count(x)
        my_dic.__setitem__(x,value)
    frequency=max(my_dic.values())
    count=0
    o=[]
    for keys in my_dic.keys():
        if my_dic[keys]==frequency:
            count+=1
            o.append(keys)
    if frequency!=1:
        if count==1:
            for keys,values in my_dic.items():
                if my_dic[keys]==frequency:
                   word=keys
        else:
            word=max(o, key=len)
        print(word,frequency)


#Provide different values for data and test your program.
data="Listen to the big clock Tick tock tick"
max_frequency_word_counter(data)