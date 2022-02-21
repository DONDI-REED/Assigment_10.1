from doctest import OutputChecker
from importlib.resources import read_text
import os

#Getting user input for the path and file name.
path = input("What is the name of the directory you want to save your file in?: ")
file = input("What is the name of the file you want to save?:  ")


#Testing to see if the path requested exists.
isExist = os.path.exists(path)
print(isExist)

if not isExist:
    #Making requested directory if it doesnt exist.
    os.makedirs(path)
    print("Directory not found, new directory has been created.")

#Make sure the current path is the users selection
cwd = os.getcwd()
print(cwd)
os.chdir(path)
print("This is the directory you selected. ",path,)

#Getting users personal information to save to a file
user_data = input("Please enter your name, address, phone number seperated with a single comma:  ")
name, address, phone_number = map(str, input("Please enter your name, address, phone number seperated with a single comma:\n").split(', '))

#Checking the proper data was passed
#print("\nYour name {}, address {}, and phone number {}, are".format(name, address, phone_number))
#print(name)
#print(address)
#print(phone_number)

#Creating file from user input
file_name = open(file , "w")
file_name.write(user_data)
file_name.close()

#print("Checking the cwd one more time:" ,path,)

#Open new file that contains users personal information and displaying it for users verification.
with open(file) as f:
    line = f.readlines()
    print("The information you entered has been pulled from the file.")
    print("This is what you entered.")    
    print(line)

