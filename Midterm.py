# CSCI 1250 Python Practicum Exam
# Student Name: Aleksandr Davis
# Date: 10/9/2025

# Score: _______/100 (max 105)

# Instructions:
# - Fill out each task below by writing Python code to answer the question.
# - Do not modify any existing code, pass is to be overwritten with your code below each function block.
# - Ensure your solutions work correctly by testing them.
# - There is a written answer section below be sure to write your answers in comments.
# - In the main() function, is available for you to call your functions.

# - When finished, please submit your .py file into the D2L Dropbox - "Midterm"


# Task 0: Ensure that your code adheres to a consistent style and coding recommendations discussed in class.
# You must use proper formatting, clear and descriptive variable names, and provide sufficient comments.
# Up to 20 points may be deducted for failing to meet these requirements.
# These 20 points are included in your total score, so no points will be lost if you follow the guidelines correctly.

#Task 1: Create a function that returns a string that answers "what is stored in a string variable?" (2 points)
def get_string():
    return "The location in memory where the string begins"

#Task 2: Print a string that would be an invalid name for a variable. (2 points)
def get_invalid_variable_name():
    print("Invalid Name")

#Task 3: Create a function that returns a list of integers from input from the user. (4 points)
def get_list():
    listOfInt = []
    
    print("Give me numbers to add 1 by 1 to a list. Type \"done\" when you are finished. \n")
    while True: 
        userChoice = input("Give me a number to add (Type 'done' to exit): " )

        if userChoice.lower() == "done":
            return listOfInt
        
        try: 
            num = int(userChoice)
            listOfInt.append(num)     

        except ValueError:
            "Please enter a valid number"
    
# Task 4: Collections and Loops (10 points)
# Write a function `sum_list(lst)` that takes a list of integers `lst` and returns the sum of all the elements in the list.
# Example: sum_list([1, 2, 3, 4, 5]) should return 15.
def sum_list():
    listOfInt = []
    total = 0

    print("Give me numbers to add 1 by 1 to a list. Type \"done\" when you are finished. \n")
    while True: 
        userChoice = input("Give me a number to add (Type 'done' to exit): ")

        if userChoice.lower() == "done":
            for num in listOfInt:
                total += num
            return total
        
        try: 
            num = int(userChoice)
            listOfInt.append(num)     

        except ValueError:
            "Please enter a valid number"

# Task 5: Decision Structures (10 points)
# Write a function `triangle_type(a, b, c)` that accepts three integer sides of a triangle.
# The function should return "equilateral" if all sides are equal, "isosceles" if only two sides are equal, 
# and "scalene" if all sides are different.
def triangle_type(a, b, c):
    triangleSides = (a, b, c)
    while True:
        a = input("What is the length of side a? ")
        b = input("What is the length of side b? ")
        c = input("What is the length of side c? ")
        if a == b and b == c:
            return "Your triangle is equilateral"
        elif a==b or b==c or c==a: 
            return "Your triangle is isoceles"
        else:
            return "your triangle is scalene"

# Task 6: Functions (10 points)
# Write a function `factorial(n)` that returns the factorial of a number `n`. Use a loop (instead of recursion) to calculate it.
# Example: factorial(5) should return 120 (since 5 * 4 * 3 * 2 * 1 = 120).
def factorial(n):
    result = 1
    for factor in range(1, n + 1):
        result *= factor
    return result

# Task 7: Input Validation (12.5 points)
# Write a function `get_valid_integer()` that repeatedly asks the user for an integer input between 1 and 100 (inclusive).
# If the user enters a value outside this range, the function should display an error message and continue asking for input
# until a valid number is entered. Once a valid number is entered, return the number.
# Example: If the user enters -5, 150, and then 50, the function should return 50.
def get_valid_integer():
    while True:
        try:
            userInput = int(input("Enter a number between 1 and 100 (inclusive): "))
            if userInput < 1 or userInput > 100:
                continue
            else:
                return userInput
        except ValueError:
            continue


# Task 8: Running Total with Input Validation (12.5 points)
# Write a function `running_total()` that continuously asks the user to enter a number.
# The function should keep a running total of all numbers entered and stop asking for input when the user enters -1.
# When -1 is entered, the function should return the total sum of all numbers entered (excluding -1).
# Example: If the user enters 5, 10, -1, the function should return 15.
def running_total():
    total = 0
    userInput = input("Enter a number to add to total. (Enter -1 when finished): ")
    while userInput != "-1":
        try: 
            num = int(userInput)
            total += num
            userInput = input("Enter a number to add to total. (Enter -1 when finished): ")
        except ValueError:
            print("Please enter a valid number")
            continue
    return total


#-------------------------------------------------------------------------------------------------------------------------------------
# Task 9: What is the difference between a syntax error and a logic error? (3 points)
# Answer in the comments below: A syntax error is similar to forgetting punctuation in
# english. Ex: forgetting a colon in a loop 
# A logic error is like using the wrong word in english. It works and makes sense but it misses the intention. 
# Ex: using a * when you ment to do addition  

# Syntax Error: for i in something
# Logic Error: 2 * 4 = 8 (6 was expected)

# Logical Operator Evaluation (1.5 points each (9 points total))
# What are the results of the following logical expressions (True or False)?

# Task 10a: True or False and True
# Answer: True

# Task 10b: not False or False and True
# Answer: True

# Task 10c: False or False and True or not True
# Answer: False

# Task 10d: True and not False or False
# Answer: True

# Task 10e: not (True or False) and (False or True)
# Answer: False

# Task 10f: True and (False or not True)
# Answer: False
#-------------------------------------------------------------------------------------------------------------------------------------

#Task 11: Write a function that does the following: (25 points)
# - Asks a user to enter the number of students.
# - For each student, ask for their name and three test scores.
# - Store this information in a list. Where the zero index is the student name, and the indices 1, 2, and 3 are the test scores.
# - Calculate the average score for each student.
# - Assign a letter grade based on the average (A = 90–100, B = 80–89, C = 70–79, D = 60–69, F = below 60).
# - Print each student’s name, their average score (rounded to 2 decimals), and their letter grade.
# - BONUS(5 points): Find the student with the highest average score, the lowest average score, and print their names at the end of the report.
def student_grades():
    pass #replace this line, including "pass" with your code


#You may test your code by calling the functions above in the main function below.
def main():
   pass #replace this line, including "pass" with your function calls. You can comment out the function calls if you wish after testing.
    

# Calls the main function (Don't Touch!!!)
if __name__ == "__main__":
    main()
