# Write your solution here
"""
Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.

The program should function as follows:
Sample output

Number 1: 2
Number 2: 1
Number 3: 6
Number 4: 7
The sum of the numbers is 16 and the mean is 4.0
"""
sum = 0
number = int(input("enter number: "))
sum += number
number = int(input("enter number: "))
sum += number
number = int(input("enter number: "))
sum += number
number = int(input("enter number: "))
sum += number

print(f"The sum of the numbers is {sum} and the mean is {sum/4}")
