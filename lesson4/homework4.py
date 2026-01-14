## Questions:

#1. <a href="https://pynative.com/python-if-else-and-for-loop-quiz/">Loops quiz</a>

#2.  What is the difference between the continue and break statements in Python?
#3. Can you explain the difference between for loop and while loop?
#4. How would you implement a nested for loop system? Provide an example.

## Homeworks:

#1.** Return uncommon elements of lists. Order of elements does not matter.

#input:
 #   list1 = [1, 1, 2]
#  list2 = [2, 3, 4]
#output: [1, 1, 3, 4]

#input:
 #   list1 = [1, 2, 3]
 #   list2 = [4, 5, 6]
#output: [1, 2, 3, 4, 5, 6]

#input:
 #   list1 = [1, 1, 2, 3, 4, 2]
 #   list2 = [1, 3, 4, 5]
#output: [2, 2, 5]
import random
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
result = []
for item in list1:
    if item not in list2:
        result.append(item)
for item in list2:
    if item not in list1:
        result.append(item)
print(result)




#**2.** Print the square of each number which is less than `n` on a separate line.


#input: n = 5
#output:
 #   1
 #  4
 # 9
 # 16
n = int(input("Enter a number: "))
for i in range(1, n):
    print(i**2)



    

#**3.** `txt` nomli string saqlovchi o'zgaruvchi berilgan.
#  `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin.
#  Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa,
#  ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.

#input: hello
#output: hel_lo

#input: assalom
#output: ass_alom

#input: abcabcdabcdeabcdefabcdefg
#output: abc_abcd_abcdeab_cdef_abcdefg

txt = input("Enter a string: ")
result = ""
vowels = "aeiouAEIOU"
for i, char in enumerate(txt):
    if i % 3 == 2:
        result += "_"
    if char in vowels or (i > 0 and txt[i-1] == "_"):
        result += "_"
    result += char
print(result)



#**4. Number Guessing Game**
#Create a simple number guessing game.
#- The computer randomly selects a number between 1 and 100. 
#- If the guess is high, print "Too high!". 
#- If the guess is low, print "Too low!". 
#- If they guess correctly, print "You guessed it right!" and exit the loop.
#- The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
#- If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.
#> Hint: Use Python’s `random.randint()` to generate the number.

number = random.randint(1, 100)
attempts = 10
while attempts > 0:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("You guessed it right!")
        break
    attempts -= 1
if attempts == 0:
    print("You lost. Want to play again? ")
play_again = input().lower()
if play_again in ['y', 'yes', 'ok']:
    exec(open('lesson4/homework4.py').read())




#**5. Password Checker**
#Task: Create a simple password checker.
#- Ask the user to enter a password. 
#- If the password is shorter than 8 characters, print "Password is too short." 
#- If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.". 
#- If the password meets both criteria, print "Password is strong."
password = input("Enter your password: ")
if len(password) < 8:
    print("Password is too short.")
elif not any(char.isupper() for char in password):
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")



#**6. Prime Numbers**
#Task: Write a Python program that prints all prime numbers between 1 and 100.
#> A prime number is a number greater than 1 that is not divisible by any number other than 1 and itself. Use nested loops to check divisibility.
prime_numbers = []
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)
print(prime_numbers)




### Bonus Challenge
#Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.
#- The computer randomly chooses `rock`, `paper`, or `scissors` using `random.choice()`.
#- The player enters their choice.
#- Display the winner and keep track of scores for the player and the computer.
#- First to 5 points wins the match.
#> Hint: Use conditionals to determine the winner based on the rules:
#> - Rock crushes Scissors
#> - Scissors cuts Paper
import random
choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0
while player_score < 5 and computer_score < 5:
    computer_choice = random.choice(choices)
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    print(f"Computer chose: {computer_choice}")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or
            (player_choice == 'scissors' and computer_choice == 'paper') or
            (player_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
    print(f"Scores => You: {player_score}, Computer: {computer_score}")
if player_score == 5:
    print("Congratulations! You won the match!")
else:
    print("Computer won the match! Better luck next time!")
