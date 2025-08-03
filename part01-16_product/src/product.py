# Fix the code
"""
This program asks the user for three numbers. The program then prints out their product, that is, the numbers multiplied by each other. There is, however, something wrong with the program - it doesn't work quite right, as you can see if you run it. Please fix it.

An example of the expected execution of the program:
Sample output

Please type in the first number: 2
Please type in the second number: 3
Please type in the third number: 5
The product is 30
"""
number = int(input("Please type in the first number: "))
product = 1
product *= number
number = int(input("Please type in the second number: "))
product *= number
number = int(input("Please type in the third number: "))
product *= number


print("The product is", product)
