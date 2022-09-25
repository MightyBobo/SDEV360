"""
Parkinson, Robert
SDEV 300 7380
27 March 2022

Week 2, Lab 2 - ...all sorts of random things, stuffed in a looped menu...
"""
import sys
import random
import string
import math
from datetime import date

#begin main_menu function
def main_menu():
    """Function to present the main menu to the user"""

    print()
    print('*************************MAIN MENU*************************')
    print()
    print('1: Generate a Secure Password')
    print('2: Calculate and Format a Percentage')
    print('3: How many days are there from today until July 4, 2025?')
    print('4: Use the Law of Cosines to calculate the leg of a triangle')
    print('5: Calculate the volume of a Right Circular Cylinder')
    print('6: Exit the Program')
    print()
#End main_menu function

#begin password_generation function
def password_generation(length,complexity):
    """Function that will generate a password based on passed variables of length,
    as well as complexity - 1 being upper case only, 2 being upper case and lower case,
    3 being upper case, lower case, and numbers, and 4 being upper case, lower case,
    numbers, and special characters"""

    #if uppercase only
    if complexity == 1:
        password = ''.join([random.choice(string.ascii_uppercase) for n in range(length)])
    #if upper and lower case
    elif complexity == 2:
        password = ''.join([random.choice(string.ascii_letters) for n in range(length)])
    #if upper case, lower case, numbers
    elif complexity == 3:
        password = ''.join([random.choice(string.ascii_letters + string.digits)\
        for n in range(length)])
    #if upper case, lower case, numbers, and special characters
    elif complexity == 4:
        password = ''.join([random.choice(string.ascii_letters + string.digits +\
        string.punctuation) for n in range(length)])

    #return the randomly generated password based on complexity
    return password
#end password_generation function

#begin calculate_percentage function
def calculate_percentage(num,den,prec):
    """Function that will calculate a percentage based on a numerator and a denominator.
    The first value passed is the numerator, second being demoninator, and the precision
    is an integer determining how many decimal places to show."""

    calculation = float(num / den) * 100
    print('*Your percentage is:', f"{calculation:.{prec}f}%*")
#end calculate_percentage function

#begin date_countdown function
def date_countdown():
    """Function that will count down the number of days remaining until the 4th of
    July, 2025, from the current date."""

    print('*Countdown days until July 4, 2025*')
    print()
    today = date.today()
    future = date(2025,7,4)
    print('*There are',(future - today).days,'days until July 4, 2025 from today.*')
    #print('There are',abs((future - today).days),'days until July 4, 2025')
#end date_countdown function

#begin cosines function
def cosines(a_side,b_side,angle):
    """Function that will calculate the length of the unknown side of a triangle,
    using the Law of Cosines.  The first value is the known A-side, second is
    the B-side, and the final value is the angle between them."""

    return math.sqrt((a_side ** 2) + (b_side ** 2) - (2 * a_side * b_side * math.cos(angle)))
#end cosines function

#begin cylinder_volume function
def cylinder_volume(radius,height):
    """Function that will calculate the volume of a right angle cylinder.
    The first value passed is the radius of the cylinder, and the second is the
    height of the cylinder."""

    return (math.pi * (radius ** 2)) * height
#end cylinder_volume function

#begin gather_integer function
def gather_integer(request):
    """Function that handles all of the input validation for gathering an integer, and
    returns it for processing when called.  The only passed variable is the string for what value
    is specifically being asked for by the user."""

    #while loop to gather an integer and do basic input validation
    while True:
        number = input(request)
        print()
        #try to convert input to an integer.  If successful, returns it.  Otherwise, turns it
        #into an arbitrary number that will flag it as invalid.  Otherwise, continue.
        try:
            number = int(number)
            return number
        except ValueError:
            return -1

        #if it's not a number
        if number.isalpha():
            return -1
#end gather_integer function

def gather_float(request):
    """Function that handles all of the input validation for gathering a float, and
    returns it for processing.  The only passed variable is the string for what value
    is specifically being asked for by the user."""

    #while loop to handle input validation until valid input is...input
    while True:
        number = input(request)
        print()

        try:
            number = float(number)
            break
        except:
            print('INVALID INPUT. Please try again')

    while True:
        if number < 0:
            print('You must enter a positive number.  Please try again.')
        else:
            break

        """if number.isalpha():
            print('INVALID INPUT. Please try again')
        #if it's not only a number, but also an integer and positive
        elif float(number) > 0:

            number = float(number)
            return number
        #else, enter valid input
        else:
            print('You must enter a positive number.  Please try again.')"""

#begin exit_program function
def exit_program():
    """Function that simply exits the program normally."""

    sys.exit(0)
#end exit_program runction

#while loop that handles our main menu re-appearing as needed
while True:
    #Call the main_menu function
    main_menu()
    selection = gather_integer('Enter a choice (1-6): ')
    print()

    #IF/ELIF section for making various menu choices
    if selection == 1:
        print('*Generate a Secure Password*')
        print()
        while True:
            pwlength = gather_integer('How many characters would you like your password to be?: ')
            #if to see if the integer is not within the acceptable limits
            if pwlength < 1:
                print('INVALID INPUT. Please try again.')
            #else to confirm password length is not 0 or negative
            else:
                break
        print('*********************Password Complexity********************')
        print('**Your password will be a combination of the below options**')
        print()
        print('1: Upper Case Only')
        print('2: Upper and Lower Case')
        print('3: Upper Case, Lower Case, Numbers')
        print('4: Upper Case, Lower Case, Special Characters')
        while True:
            pwcomplexity = gather_integer('How complex would you like your password? (1-4): ')
            #if to see if the integer is not within the acceptable limits
            if pwcomplexity < 1 or pwcomplexity > 4:
                print('INVALID INPUT. Please try again.')
            #else that calls the password_generation function and displays the results
            #to the user
            else:
                print('Your password is:',password_generation(pwlength,pwcomplexity))
                print()
                break
    #else if the user wants to calculate a percentage
    elif selection == 2:
        print('*Calculate and Format a Percentage*')
        print()
        numerator = gather_float('Please enter your numerator: ')
        denominator = gather_float('Please enter your denominator: ')
        while True:
            decimal_places = gather_integer('Please enter the number of decimal places to show: ')
            if decimal_places < 0:
                print('INVALID INPUT. Please enter a positive number or 0.')
            else:
                break
        calculate_percentage(numerator,denominator,decimal_places)
    #else if the user wants to use the date countdown feature
    elif selection == 3:
        date_countdown()
    #else if the user wants to use the law of cosines feature
    elif selection == 4:
        print('*Use the Law of Cosines to calculate the leg of a triangle*')
        print()
        known_a = gather_float('Please enter the length of the A-side of the triangle: ')
        known_b = gather_float('Please enter the length of the B-side of the triangle: ')
        #while to make sure you aren't entering an impossible angle...
        while True:
            known_angle = gather_float('Please enter the angle of the corner between A and B: ')
            #if angle is an acceptable amount, break the while loop.  Otherwise, print error.
            if known_angle >= 180 or known_angle <= 0:
                print('INVALID ANGLE.  Please enter an amount greater than 0, and less than 180.')
            else:
                break
        print('*The length of the leg of the triangle is:',cosines(known_a,known_b,\
        known_angle),'*')
    #else if the user wants to calculate the volume of a right cylinder
    elif selection == 5:
        print('*Calculate the volume of a Right Circular Cylinder*')
        print()
        known_height = gather_float('Please enter the height of the cylinder: ')
        known_radius = gather_float('Please enter the radius of the cylinder: ')
        print('The volume of your right circular cylinder is:',\
        cylinder_volume(known_radius,known_height))
    #else if the user wants to exit the program
    elif selection == 6:
        print('Thank you for using the program.  Goodbye!')
        exit_program()
    #ELIF specifically for any numbers outside of the acceptable range
    elif selection < 1 or selection > 6:
        print('INVALID INPUT. Please try again.')
    