### Zero Check Decorator

#Write a decorator function called `check`
#  that verifies that the denominator is not equal to 0 and apply it to the following function:

#python
#@check
#def div(a, b):
#   return a / b



#input: div(6, 2)
#output: 3



#input: div(6, 0)
#output: "Denominator can't be zero"

def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper
@check
def div(a, b):
    return a / b
                                                      


#############################################################################################
###############################################################################################

### **Employee Records Manager**
#**Objective**: Create a program to manage employee records using file handling.  

#**Tasks**:  
#1. **File Creation and Data Entry**  
 #  - Create a file named **"employees.txt"**.  
  # - Allow the user to add new employee records. Each record should have the following fields:  
   #  
    # Employee ID, Name, Position, Salary
     
   #  Example of a record:  
     
   #  1001, John Doe, Software Engineer, 75000

     
###############################################################################################
#################################################################################################
#2. **Menu Options**  
   #Your program should present the following options:  
   
   #1. Add new employee record
   #2. View all employee records
   #3. Search for an employee by Employee ID
   #4. Update an employee's information
   #5. Delete an employee record
   #6. Exit

################################################################################################
################################################################################################ 

#3. **Functional Requirements**  
 #  - **Option 1**: Append a new employee record to **"employees.txt"**.  
 #  - **Option 2**: Display all employee records from **"employees.txt"**.  
 #  - **Option 3**: Allow the user to search for an employee by **Employee ID** and display their details.  
 #  - **Option 4**: Update an employee’s information (name, position, or salary) based on the Employee ID.  
 #  - **Option 5**: Delete an employee's record from the file using the Employee ID.  
 #  - **Option 6**: Exit the program. 
import os
def add_employee():
      with open("employees.txt", "a") as file:
         emp_id = input("Enter Employee ID: ")
         name = input("Enter Name: ")
         position = input("Enter Position: ")
         salary = input("Enter Salary: ")
         file.write(f"{emp_id}, {name}, {position}, {salary}\n")
      print("Employee record added successfully.")
def view_employees():
      if not os.path.exists("employees.txt"):
          print("No employee records found.")
          return
      with open("employees.txt", "r") as file:
          records = file.readlines()
          if not records:
              print("No employee records found.")
              return
          for record in records:
              print(record.strip())
def search_employee():

      emp_id = input("Enter Employee ID to search: ")
      if not os.path.exists("employees.txt"):
          print("No employee records found.")
          return
      with open("employees.txt", "r") as file:
          records = file.readlines()
          for record in records:
              if record.startswith(emp_id + ","):
                  print("Employee found:", record.strip())
                  return
          print("Employee not found.")
def update_employee():
      emp_id = input("Enter Employee ID to update: ")
      if not os.path.exists("employees.txt"):
          print("No employee records found.")
          return
      updated = False
      with open("employees.txt", "r") as file:
          records = file.readlines()
      with open("employees.txt", "w") as file:
          for record in records:
              if record.startswith(emp_id + ","):
                  name = input("Enter new Name: ")
                  position = input("Enter new Position: ")
                  salary = input("Enter new Salary: ")
                  file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                  updated = True
              else:
                  file.write(record)
      if updated:
          print("Employee record updated successfully.")
      else:
          print("Employee not found.")
def delete_employee():
      emp_id = input("Enter Employee ID to delete: ")
      if not os.path.exists("employees.txt"):
          print("No employee records found.")
          return
      deleted = False
      with open("employees.txt", "r") as file:
          records = file.readlines()
      with open("employees.txt", "w") as file:
          for record in records:
              if record.startswith(emp_id + ","):
                  deleted = True
              else:
                  file.write(record)
      if deleted:
          print("Employee record deleted successfully.")
      else:
          print("Employee not found.")
def main():    
      while True:
          print("\nEmployee Records Manager")
          print("1. Add new employee record")
          print("2. View all employee records")
          print("3. Search for an employee by Employee ID")
          print("4. Update an employee's information")
          print("5. Delete an employee record")
          print("6. Exit")
          choice = input("Enter your choice (1-6): ")
          if choice == '1':
              add_employee()
          elif choice == '2':
              view_employees()
          elif choice == '3':
              search_employee()
          elif choice == '4':
              update_employee()
          elif choice == '5':
              delete_employee()
          elif choice == '6':
              print("Exiting the program.")
              break
          else:
              print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()


###############################################################################################
###############################################################################################

### **Word Frequency Counter**
#**Objective**: Analyze a text file and count how often each word appears.  

#**Tasks**:  
#1. **File Input**  
#   - Use the file **"sample.txt"**. The file can contain any text (like a paragraph or an article).  
#   - If **"sample.txt"** does not exist, prompt the user to create it by typing in a paragraph.  

#2. **Count Word Frequency**  
 #  - Read the file content and split it into individual words.  
 #  - Count the frequency of each word (ignore capitalization, e.g., "The" and "the" should be counted as the same word).  
  # - Ignore punctuation (like commas, periods, etc.).  

#3. **Output**  
 #  - Display the total number of words in the file.  
 #  - Display the top 5 most common words with their counts.  
 #  - Save the output to a new file called **"word_count_report.txt"**.  

#4. **Example Output**  
  # **Content of sample.txt**:  
   
  # This is a simple file.
  # This file, is for testing purposes. It is a test file.
   

  # **Console Output**:  
   
  # Total words: 14
  # Top 5 most common words:
  # is - 3 times
  # this - 2 times
  # file - 3 times
  # a - 2 times
  # test - 1 time
   

  # **Content of word_count_report.txt**:  
   
  # Word Count Report
  # Total Words: 14
  # Top 5 Words:
  # is - 3
  # file - 3
  # this - 2
  # a - 2
  # test - 1
import os
import string
from collections import Counter
def create_sample_file():
    paragraph = input("sample.txt not found. Please enter a paragraph to create the file:\n")
    with open("sample.txt", "w") as file:
        file.write(paragraph)
def count_word_frequency():
      if not os.path.exists("sample.txt"):
         create_sample_file()
      with open("sample.txt", "r") as file:
         content = file.read().lower()
      translator = str.maketrans('', '', string.punctuation)
      words = content.translate(translator).split()
      total_words = len(words)
      word_counts = Counter(words)
      most_common = word_counts.most_common(5)
      print(f"Total words: {total_words}")
      print("Top 5 most common words:")
      for word, count in most_common:
         print(f"{word} - {count} times")
      with open("word_count_report.txt", "w") as report:
         report.write("Word Count Report\n")
         report.write(f"Total Words: {total_words}\n")
         report.write("Top 5 Words:\n")
         for word, count in most_common:
               report.write(f"{word} - {count}\n")
if __name__ == "__main__":
      count_word_frequency()


######################################################################################################
#######################################################################################################
#**Bonus Task**:  
#- Allow the user to specify how many "top common words" to display (e.g., top 3, top 10, etc.).  
#- Make sure the program ignores case, punctuation, and handles large files efficiently.
import os
import string
from collections import Counter
def create_sample_file():
    paragraph = input("sample.txt not found. Please enter a paragraph to create the file:\n")
    with open("sample.txt", "w") as file:
        file.write(paragraph)
def count_word_frequency(top_n=5):
      if not os.path.exists("sample.txt"):
         create_sample_file()
      with open("sample.txt", "r") as file:
         content = file.read().lower()
      translator = str.maketrans('', '', string.punctuation)
      words = content.translate(translator).split()
      total_words = len(words)
      word_counts = Counter(words)
      most_common = word_counts.most_common(top_n)
      print(f"Total words: {total_words}")
      print(f"Top {top_n} most common words:")
      for word, count in most_common:
         print(f"{word} - {count} times")
      with open("word_count_report.txt", "w") as report:
         report.write("Word Count Report\n")
         report.write(f"Total Words: {total_words}\n")
         report.write(f"Top {top_n} Words:\n")
         for word, count in most_common:
               report.write(f"{word} - {count}\n")
if __name__ == "__main__":
      try:
          top_n = int(input("Enter the number of top common words to display: "))
      except ValueError:
          top_n = 5
      count_word_frequency(top_n)

      