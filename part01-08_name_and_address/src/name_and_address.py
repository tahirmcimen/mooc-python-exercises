# Write your solution here
"""
Please write a program which asks for the user's name and address. The program should also print out the given information, as follows:
Sample output

Given name: Steve
Family name: Sanders
Street address: 91 Station Road
City and postal code: London EC05 6AW
Steve Sanders
91 Station Road
London EC05 6AW

"""
name = input("What is your name?")
familyname = input("What is your family name?")
address = input("What is your address?")
citycode = input("What is your city code?")
print(name + " " + familyname)
print(address)
print(citycode)
