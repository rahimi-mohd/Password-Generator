# simple password gene
import random, datetime, sys

# lower case
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# upper case list from lower_case list
upper_case = []
for alpa in lower_case:
    upper_case.append(alpa.upper())

# print(upper_case) for debug

# symbols
symbols = ['!', '#', '$', '&', '*', '?', '<', '>'] # add more symbols if you need more

# program main loop
while True:
    print("+------------------+")
    print("|Password generator|")
    print("+------------------+\n")
    lower_count = int(input("How many lower case in password: "))
    upper_count = int(input("How many upper case in password: "))
    sym_count = int(input("How many symbols in password: "))

    # insert alphabets and symbols into new_password based on user input
    new_password = []

    for alpa in range(lower_count):
        new_password.append(random.choice(lower_case))
    
    for alpa in range(upper_count):
        new_password.append(random.choice(upper_case))

    for sy in range(sym_count):
        new_password.append(random.choice(symbols))
        

    # shuffle and join new pasword list
    random.shuffle(new_password)
    # print("".join(new_password))
    
    # save new password into text file
    pass_for = input("Save password for: ")
    today = datetime.datetime.now()
    today_date = today.strftime("%d-%m-%Y")

    # open text file
    with open ("password.txt", 'a') as p:
        p.write(f"Password for : {pass_for}\n")
        p.write(f"Date: {today_date}\n")
        p.write(f"Generate password : {''.join(new_password)}\n\n")

    # quit or continue program
    print("Press any key to generate more password or 'q' to quit program")
    quit_program = input(":> ").lower()
    if quit_program == 'q':
        print("\nTerminating program....")
        print("Thank you for using Password Generator....")
        sys.exit()
        



