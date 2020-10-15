# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

Name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
Current_year = int(input("Enter the Current year: "))
Diff = 100 - age
Centenary_celebration = Current_year + Diff
print("You celebrate your 100 years :" + str(Centenary_celebration))

