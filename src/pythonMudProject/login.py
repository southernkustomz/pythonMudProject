import csv
from accounts import Account

un = None
pw = None
all_users = []

# Function to create a new account.
def create_account(username):
    password = ''

    # Open a csv file containing a list of usernames and passwords
    f = open(account_list,mode='a',newline='')
    csv_writer = csv.writer(f)

    # set variables for password confirmation
    pw1 = ''
    pw2 = None

    # Check to see if the password attempts match
    while pw1 != pw2:
        pw1 = input("Enter a password: ")
        pw2 = input("Please re-enter your password: ")

        # if passwords match, create an account using the password
        if pw1 == pw2:
            password = pw2
            print("Account created successfully!")
        else:
            print("Those passwords do not match, try again.")

    # Write the new username and password to the csv file as a row and then close the file.
    csv_writer.writerow([username,password])
    f.close()
    #player = Account(username,password)

# Main Login Script
login = False
while login == False:
    un = input("Username: ")

    # Open the csv file and format it into a list of lists.
    account_list = r'C:\Users\south\PycharmProjects\pythonMudProject\accounts.csv'
    data = open(account_list, encoding='utf-8')
    csv_data = csv.reader(data)
    data_lines = list(csv_data)

    for line in data_lines[1:len(data_lines)]:
        # Add all usernames to the all_users list.
        all_users.append(line[0])
    print(all_users)

        # checking the username column of the csv file for a match to the un variable
    for line in data_lines[1:len(data_lines)]:
        # If there is a match ask for a password
        if line[0] == un:
            pw = input("Password: ")

            # Allow 3 password attempts if password does not match the user
            incorrect_count = 0
            while pw != line[1]:
                print("Incorrect Password!")
                pw = input("Password: ")
                incorrect_count += 1
                if incorrect_count >= 2:
                    print("Too many password attempts!")
                    data.close()
                    quit()

            # If username and password match login is successful.
            else:
                print('Login Successful!')
                data.close()
                login = True

        # If username does not exist, ask if user wants to create an account
        elif un not in all_users:
            create = input("That username does not exist.\nWould you like to create a new user? (Y or N): ")
            if create.lower().startswith('y'):
                data.close()
                create_account(un)
                login = True
                break

            # If choice is not y, ask for username again.
            else:
                un = input("Username: ")
                continue

        else:
            continue
