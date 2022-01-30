#You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item for amount z. 
# The shopkeeper wants you to provide exact change. You want to pay using minimum number of coins. 
# How many 5 rupee coins and 1 rupee coins will you use? If exact change is not possible then display -1.

#PROGRAM

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    if rupees_to_make>no_of_five*5+no_of_one:     #checking rupees_to_make is more than total sum of rupees made by coins
        print(-1)
    else:
        a=rupees_to_make//5                       #no of 5 rupee coins required
        if a<no_of_five:                          #checking if required 5 Rs coins is more than given 5 Rs coins
            five_needed_1=a
        else:
            five_needed_1=no_of_five
        o=rupees_to_make-five_needed_1*5          
        if o<no_of_one:                           
            one_needed_1=o                        #no of 1 rupee coins required
        else:
            one_needed_1=no_of_one
        x=one_needed_1+five_needed_1
        p=one_needed_1+five_needed_1*5
        b=rupees_to_make
        if b<no_of_one:
            one_needed_2=b
        else:
            one_needed_2=no_of_one
        m=rupees_to_make-one_needed_2
        q=m//5
        if q<no_of_five:
            five_needed_2=q
        else:
            five_needed_2=no_of_five
        y=five_needed_2+one_needed_2
        q=one_needed_2+five_needed_2*5
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
        if (p==rupees_to_make and q==rupees_to_make) or (p==rupees_to_make or q==rupees_to_make) :         #checking which calculation required min no of coins
            if p==rupees_to_make and q==rupees_to_make:
                if x>y:
                   five_needed=five_needed_2
                   one_needed=one_needed_2
                else:
                   five_needed=five_needed_1
                   one_needed=one_needed_1
            elif p==rupees_to_make:
                five_needed=five_needed_1
                one_needed=one_needed_1
            else: 
                five_needed=five_needed_2
                one_needed=one_needed_2
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        else:
            print(-1)
            
        
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)