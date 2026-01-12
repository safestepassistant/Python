# Lesson 2 Homework Solutions

### Number Data Type Questions

#1. Create a program that takes a float number as input and rounds it to 2 decimal places.
float_number = float(input("Enter a float number: "))
rounded_number = round(float_number, 2)
print("Rounded number:", rounded_number)

#2. Write a Python file that asks for three numbers and outputs the largest and smallest.
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))
print("Largest number:", max(number1, number2, number3))
print("Smallest number:", min(number1, number2, number3))

#3. Create a program that converts kilometers to meters and centimeters.
kilometers = float(input("Enter distance in kilometers: "))
meters = kilometers * 1000
centimeters = kilometers * 100000
print("Distance in meters:", meters)
print("Distance in centimeters:", centimeters)

#4. Write a program that takes two numbers and prints out the result of integer division and theremainder.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Integer division result:", num1 // num2)
print("Remainder:", num1 % num2)   

#5. Make a program that converts a given Celsius temperature to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#6. Create a program that accepts a number and returns the last digit of that number.
number = int(input("Enter a number: "))
last_digit = abs(number) % 10
print("Last digit of the number:", last_digit)

#7. Create a program that takes a number and checks if it’s even or not.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


########################################################################################################
########################################################################################################
########################################################################################################

### String Questions:

#1. Create a program to ask name and year of birth from user and tell them their age.
name =input("enter your name: ")
birth_date=int(input("please, enter your birth year: "))
age=2026-birth_date
print(f"your name is {name} and your age is {age}")

#2. Extract car names from this text: txt = 'LMaasleitbtui'
txt = 'LMaasleitbtui'
car_names = txt[1::2]
print("Extracted car names:", car_names)

#3. Write a Python program to:
  # - Take a string input from the user.
  # - Print the length of the string.
 #  - Convert the string to uppercase and lowercase.
user_string = input("Enter a string: ")
print("Length of the string:", len(user_string))
print("Uppercase:", user_string.upper())
print("Lowercase:", user_string.lower())

#4. Write a Python program to check if a given string is `palindrome` or not.
#> What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.
user_string = input("Enter a string: ")
if user_string == user_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#5. Write a program that counts the number of vowels and consonants in a given string.
user_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0   
for char in user_string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)

#6. Write a Python program to check if one string contains another.
user_string = input("Enter a string: ")
word = input("Enter a word to check: ")
if word in user_string:
    print("The word is found in the string.")
else:
    print("The word is not found in the string.")

#7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.  
#Example:  
   #- Input sentence: "I love apples."  
   # - Replace: "apples"  
  # - With: "oranges"  
  # - Output: "I love oranges."
sentence = input("Enter a sentence: ")
word_to_replace = input("Enter a word to replace: ")
replacement_word = input("Enter the replacement word: ")
new_sentence = sentence.replace(word_to_replace, replacement_word)
print("Modified sentence:", new_sentence)

#8. Write a program that asks the user for a string and prints the first and last characters of the string.  
user_string = input("Enter a string: ")
if len(user_string) > 0:
    print("First character:", user_string[0])
    print("Last character:", user_string[-1])

#9. Ask the user for a string and print the reversed version of it.
user_string = input("Enter a string: ")
reversed_string = user_string[::-1]
print("Reversed string:", reversed_string)

#10. Write a program that asks the user for a sentence and prints the number of words in it. 
user_sentence = input("Enter a sentence: ") 
words = user_sentence.split()
print("Number of words in the sentence:", len(words))

#11. Write a program to check if a string contains any digits. 
user_string = input("Enter a string: ")
contains_digit = any(char.isdigit() for char in user_string) 
if contains_digit:
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")

#12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., `-` or `,`).  
words = input("Enter words separated by spaces: ").split()
separator = input("Enter a separator character (e.g., '-', ','): ")
joined_string = separator.join(words)
print("Joined string:", joined_string)

#13. Ask the user for a string and remove all spaces from it.  
user_string = input("Enter a string: ")
string_without_spaces = user_string.replace(" ", "")
print("String without spaces:", string_without_spaces)

#14. Write a program to ask for two strings and check if they are equal or not.  
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string1 == string2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")
    

#15. Ask the user for a sentence and create an acronym from the first letters of each word.  
  #  Example:  
  #  - Input: "World Health Organization"  
  # - Output: "WHO"  
sentence = input("Enter a sentence: ")
words = sentence.split()
acronym = "".join(word[0].upper() for word in words)
print("Acronym:", acronym)

#16. Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.  
user_string = input("Enter a string: ")
char_to_remove = input("Enter a character to remove: ")
modified_string = user_string.replace(char_to_remove, "")
print("Modified string:", modified_string)

#17. Ask the user for a string and replace all the vowels with a symbol (e.g., `*`).  
user_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
modified_string = "".join("*" if char in vowels else char for char in user_string)
print("Modified string:", modified_string)

#18. Write a program that checks if a string starts with one word and ends with another.  
 #   Example:  
 #   - Input: "Python is fun!"  
  #  - Starts with: "Python"  
 #   - Ends with: "fun!"  
user_string = input("Enter a string: ")
start_word = input("Enter the starting word: ")
end_word = input("Enter the ending word: ")
if user_string.startswith(start_word) and user_string.endswith(end_word):
    print("The string starts with '{}' and ends with '{}'.".format(start_word, end_word))
else:
    print("The string does not start with '{}' and end with '{}'.".format(start_word, end_word))
    


########################################################################################################
########################################################################################################
########################################################################################################
 ### Boolean Data Type Questions:
#1. Write a program that accepts a username and password and checks if both are not empty.
username = input("Enter username: ")
password = input("Enter password: ")   
if username and password:
    print("Username and password are not empty.")  
else:
    print("Username or password is empty.")
    
#2. Create a program that checks if two numbers are equal and outputs a message if they are.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))   
if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")
    
#3. Write a program that checks if a number is positive and even.
number = int(input("Enter a number: "))
if number > 0 and number % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number is not positive and even.")
    
#4. Write a program that takes three numbers and checks if all of them are different.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 != num2 and num1 != num3 and num2 != num3:
    print("All numbers are different.")
else:
    print("Some numbers are the same.")
    
#5. Create a program that accepts two strings and checks if they have the same length.
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if len(string1) == len(string2):
    print("The strings have the same length.")
else:
    print("The strings do not have the same length.")
    
#6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")
    
#7. Write a program that checks if the sum of two numbers is greater than 50.8.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if (num1 + num2) > 50.8:
    print("The sum of the numbers is greater than 50.8.")
else:
    print("The sum of the numbers is not greater than 50.8.")

#8 Create a program that checks if a given number is between 10 and 20 (inclusive)
number = float(input("Enter a number: "))
if 10 <= number <= 20:
    print("The number is between 10 and 20 (inclusive).")
else:
    print("The number is not between 10 and 20 (inclusive).")
