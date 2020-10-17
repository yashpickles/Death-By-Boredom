# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

def palindrome_or_not(string):
    lenght = len(string)
    first = 0
    last = lenght - 1
    status = 1
    while first < last:
        if string[first] == string[last]:
            first = first + 1
            last = last - 1
        else:
            status = 0
            break
    return int(status)


string = input("Enter a string: ")
print("Method 2")
status = (palindrome_or_not(string))

if (status):
    print("It is a Palindrome! ")
else:
    print(" It is not a Palindrome! ")
