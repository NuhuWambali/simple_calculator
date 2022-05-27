#this is a simple calculator built by nuhu

#welcome text on the screen
print("""  
    ***************************************
    *                                     *
    *      WELCOME TO NUHU PROGRAMING     *
    *                                     *
    ***************************************
  Enter 1 : summation
  Enter 2 : substraction
  Enter 3 : multiplication
  Enter 4 : division
  
  """)

#asking user input and checking value error
try:
    userinput=int(input("Please select an above option :\n"))
except ValueError:
    exit("\n hey! that's not a number")
else:
     print("\n")
#checking userinput matching with choices
if userinput > 4 or userinput < 1:
    print("wrong choice")
    exit()
elif userinput == 1:
    print("you choose summation")
elif userinput == 2:
    print("you choose substraction")
elif userinput == 3:
    print("you choose multiplication")
else:
    print("you choose division")
#creating a function for choices and calculate the task choosen
def choice():
    try:
        first_number = int(input("enter the first number"))
    except ValueError:
        exit("hey! that's not a number")
    else:
        print(" ")
    try:
        second_number = int(input("enter the second number"))
    except ValueError:
        exit("hey! that's not a number")
    else:
     print(" ")
     #creating function to catch zero division error
     def zerodivision(first_number,second_number):
         try:
            div = first_number / second_number
         except ZeroDivisionError:
             print(f"division of {first_number} and {second_number} is UNDEFINED")
         else:
            print(f"division of {first_number} and {second_number} is {div}")
    #using if condition to check for userinput
    if userinput == 1:
     sum=first_number + second_number
     print(f"the sum of {first_number} and {second_number} is {sum}")
    elif userinput == 2:
     sub = first_number - second_number
     print(f"substraction of {first_number} and {second_number} is {sub}")
    elif userinput == 3:
     mut = first_number * second_number
     print(f"the multiplication of {first_number} and {second_number} is {mut}")
    else:
     zerodivision(first_number,second_number)
def goodbye():
    print("""
    ----------------------------------
    - THANK YOU FOR USING OUR SYSTEM - 
    - contact developer via whatsapp -
    -        +255688 349 680         -
    ----------------------------------
    """)
choice()
goodbye()
#BROUGH TO YOU BY NUHU WAMBALI