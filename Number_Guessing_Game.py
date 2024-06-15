import random
import math

#getting ranges
a=int(input("\nLower bound number:"))
b=int(input("Upper bound number:"))

#generating random
x=random.randint(a,b)

#minimum number of guesses
min=round(math.log(b-a+1,2))

#print the number of guesses
print("\n\tYou've only %d chances to guess the number!\n"%min)

#while condition for checking
c=0
while c<min:
    guess=int(input("Guess a number:-"))
    if x==guess:
        print("\n\t--- Congrats you found in %d try ---" %(c+1))
        print("\t    --- The number is: %d ---\n"%x)
        break
    elif x<guess:
        print("The guess is too high!\n")
    elif x>guess:
        print("The guess is too low!\n") 
    c+=1   

#if number of guess exceeded
if c>=min:
    print("\t--- The number is: %d ---"%x)
    print("\t   --- TRY AGAIN? ---")      

