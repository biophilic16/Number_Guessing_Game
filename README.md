Project Objective:
User selects a range, i.e., from A to B, where A and B belong to Integer.
Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses.

Formula for finding minimun guesses:
Minimum number of guessing = log2(Upper bound – lower bound + 1)

Algorithm: 
User inputs the lower bound and upper bound of the range.
The compiler generates a random integer between the range.
For repetitive guessing, a while loop will be initialized.
If the user guessed a number which is greater than a randomly selected number, the user gets an output “You guessed too high!“
Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “ou guessed too small!”
And if the user guessed in a minimum number of guesses, the user gets a “Congrats! ” Output.
Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “TRY AGAIN?” output with the ramdom number displayed.


