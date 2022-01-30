#Write a python program to solve a classic ancient Chinese puzzle.
#We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

#PROGRAM

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    data=0
    for i in range(heads+1):
        x=heads-i
        if 2*i+4*x==legs:     
            chicken_count=i
            rabbit_count=x
            print(chicken_count,rabbit_count)
            data=1
    if data==0:
        print(error_msg)

#Provide different values for heads and legs and test your program
solve(38,131)