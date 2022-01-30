#Exercise_on_String-Level-2
#Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
#The ticket number should be generated as airline:src:dest:number
#where
#Consider AI as the value for airline
#src and dest should be the first three characters of the source and destination cities.
#number should be auto-generated starting from 101
#The program should return the list of ticket numbers of last five passengers.
#Note: If passenger count is less than 5, return the list of all generated ticket numbers.
#Example:   sample Input:  airline = AI ,source = Bangalore ,destination = London ,no_of_passengers = 10
#           sample output: ['AI:Ban:Lon:106', 'AI:Ban:Lon:107', 'AI:Ban:Lon:108', 'AI:Ban:Lon:109', 'AI:Ban:Lon:110']

#PROGRAM

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    if no_of_passengers<5:
        x=no_of_passengers
        for i in range(1,x+1):
            e=airline
            b=source[:3]
            c=destination[:3]
            d=int(100+i)
            a=e+":"+b+":"+c+":"+str(d)
            ticket_number_list.append(a)
    else:
        x=no_of_passengers-4
        for i in range(x,no_of_passengers+1):
            e=airline
            b=source[:3]
            c=destination[:3]
            d=int(100+i)
            a=e+":"+b+":"+c+":"+str(d)
            ticket_number_list.append(a)
    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))