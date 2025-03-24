#Create a Personalized Greeting

#Function to concate firstname and lastname and return a statement
def printName(firstName, lastName):
    return f"Hello, {firstName+ " " +lastName}! Welcome to the Python Program."

#Input firstname and lastname capitalizing each while striping them of any whitespaces 
firstName = input("Enter First Name: ").strip().capitalize()
lastName = input("Enter Second Name: ").strip().capitalize()

#Conditional statement to ensure that firstname and lastname are alphabets
if  not(firstName.isalpha() and lastName.isalpha()):
    print("First and Last Names must only be alphabets!")
else:
    result = printName(firstName, lastName)
    print(result)
