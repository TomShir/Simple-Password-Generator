#Create a Password generator from given information using Python 
from colorama import Fore 
import time 
import sys 
color_names=['teal','blue','green','yellow','red','orange','magenta','pink','purple','turquoise','black','grey','white','teal'.upper(),'blue'.upper(),'green'.upper(),'yellow'.upper(),'red'.upper(),'orange'.upper(),'magenta'.upper(),'pink'.upper(),'purple'.upper(),'turquoise'.upper(),'black'.upper(),'grey'.upper(),'white'.upper(),'teal'.title(),'blue'.title(),'green'.title(),'yellow'.title(),'red'.title(),'orange'.title(),'magenta'.title(),'pink'.title(),'purple'.title(),'turquoise'.title(),'black'.title(),'grey'.title(),'white'.title()]
def loop_over(sequence,color,delay_time):

    for text in sequence:
        sys.stdout.flush()
        time.sleep(delay_time)
        sys.stdout.write(f'{color}{text}')
    else:
        print(f'{Fore.RESET}')
numbers=list(range(1,11,1))
try:
    enter_number=int(input('Enter a number between 1 and 10:'))
    while enter_number not in numbers:
        loop_over('Please enter a number between 1 and 10')
        time.sleep(1)
        enter_number_1=input('Enter a number between 1 and 10:')
        if enter_number_1 in numbers:
            break 
    else:
        colour_name=input('Enter the name of your favourite color:')
        length_of_colour_name=len(colour_name)
        if length_of_colour_name<2 or length_of_colour_name>10:
           loop_over(sequence='The name of your favourite color needs to be between 2 to 10 characters long',color=Fore.RED,delay_time=0.1)
        elif colour_name not in color_names: 
            loop_over(sequence='Not a valid colour name',color=Fore.RED,delay_time=0.1)
        else:
             def generate_password(number,colour):
                 loop_over(sequence=f'Your generated password based on given information:{str(number)+colour+time.asctime()[-4:]}',color=Fore.GREEN,delay_time=0.1)
                 
                 
             if enter_number:
                generate_password(number=enter_number,colour=colour_name)
             elif enter_number_1:
                generate_password(number=enter_number_1,colour=colour_name)
                     
except ValueError:
    time.sleep(1)
    loop_over(sequence='Error,a numerical value was not entered',color=Fore.RED,delay_time=0.1)