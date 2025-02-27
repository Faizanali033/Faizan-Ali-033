
# Function to check if a number is positive, negative, or zero:
# Taking user input
num = float(input("Enter a Number: "))

# Checking if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Function to check if a year is a leap year
# Taking user input
year = int(input("Enter a year: "))

# Checking if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# Get marks from the user
marks = float(input("Enter your marks: "))

# Determine the grade
if marks >= 85:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

# Print the grade
print(f"Your grade is: {grade}")