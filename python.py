# Day-014
# Date-11/12/2023
# Time-17:33 pm
# ifelse conditional statements


#programm to find your age group
age=int(input("Enter your age in whole number:"))
if(age==0 or age==1):
  print("You are Infant")
elif(age>=2 and age<=4):
  print("You are Toddler")
elif(age>=5 and age<=12):
  print("You are Child")
elif(age>=13 and age<=19):
  print("You are Teen")
elif(age>=20 and age<=39):
  print("You are Adult")
elif(age>=40 and age<=59):
  print("You are Middle Age Adult ")
elif(age>=60 and age<=110):
  print("You are Senior Adult")
else:
  print("Seriously,You are alive!")

#programm to find the integer number is zero or positive or negative
integer_number=int(input("Enter any integer number :"))
if(integer_number>0):
  print("Entered number is Positive")
if(integer_number<0):
  print("Entered number is Negetive")
if(integer_number==0):
  print("Entered number is Zero")


import time
timestamp=time.strftime('%H:%M:%S')
print("Time :",timestamp)

hour=int(time.strftime('%H'))
min=int(time.strftime('%M'))

if(hour>=5 and hour<=11 and min>=0 and min<=59):
  print("Good Morning Sir")

if(hour>=12 and hour<=17 and min>=0 and min<=59):
  print("Good Afternoon Sir")

if(hour>=18 and hour<=23 and hour>=0 and hour<=4 and min>=0 and min<=59):
  print("Good Evening Sir")



size = input("What size of pizza do you want (S/M/L)? ")
bill = 0

if size.upper() == "S":
    bill = 100
elif size.upper() == "M":
    bill = 200
elif size.upper() == "L":
    bill = 350
else:
    print("Invalid size selection. Please choose S, M, or L.")

if bill != 0:
    print(f"Your bill for the {size.upper()}-sized pizza is: rs{bill}")
    toppings = input("Do you want to add extra toppings? (Y/N) ")
    if toppings.upper() == "Y":
        bill += 50
    coke = input("Do you want to add a coke? (Y/N) ")
    if coke.upper() == "Y":
        bill += 20
    chesse = input("Do you want to add a chesse? (Y/N) ")
    if chesse.upper() == "Y":
        bill += 120
    sauce = input("Do you want to add sauce? (Y/N) ")
    if sauce.upper() == "Y":
        bill += 10

    print(f"Your updated bill is: rs{bill}")



import random

letters = ['q','w','e','r','t','y','u','i','o','p', 'a','s','d','f','g','h','j','k','l',
           'z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P',
           'A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

numbers = ['1','2','3','4','5','6','7','8','9','0']

symbols = ['!','*','&','%','$','#','@']

print("Welcome to Password Generator:")

L = int(input("How many letters do you want: "))
S = int(input("How many symbols do you want: "))
N = int(input("How many numbers do you want: "))

password = ""

for i in range(1, L+1):
    char = random.choice(letters)
    password += char

for i in range(1, N+1):
    char = random.choice(numbers)
    password += char

for i in range(1, S+1):
    char = random.choice(symbols)
    password += char


print("Your generated password is:", password)




import random

letters = ['q','w','e','r','t','y','u','i','o','p', 'a','s','d','f','g','h','j','k',
           'l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P',
           'A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

numbers = ['1','2','3','4','5','6','7','8','9','0']

symbols = ['!','*','&','%','$','#','@']

print("Welcome to Password Generator:")

L = int(input("How many letters do you want: "))
S = int(input("How many symbols do you want: "))
N = int(input("How many numbers do you want: "))
#to make a str with nub char symb
allchar = letters + numbers + symbols
#random function to suffel all together
random.shuffle(allchar)

password = ""

for i in range(L):
    char = random.choice(allchar)
    password += char

for i in range(N):
    char = random.choice(allchar)
    password += char

for i in range(S):
    char = random.choice(allchar)
    password += char

print("Your generated password is:", password)






class CoffeeMachine:
    def __init__(self):
        self.water = 1000
        self.coffee_beans = 500
        self.milk = 500
        self.cups = 20

    def make_coffee(self, coffee_type):
        if coffee_type == "espresso":
            if self.water >= 50 and self.coffee_beans >= 20 and self.cups >= 1:
                print("Making espresso...")
                self.water -= 50
                self.coffee_beans -= 20
                self.cups -= 1
                print("Here is your espresso! Enjoy!")
            else:
                print("Sorry, not enough ingredients to make espresso.")
        elif coffee_type == "latte":
            if self.water >= 100 and self.coffee_beans >= 20 and self.milk >= 150 and self.cups >= 1:
                print("Making latte...")
                self.water -= 100
                self.coffee_beans -= 20
                self.milk -= 150
                self.cups -= 1
                print("Here is your latte! Enjoy!")
            else:
                print("Sorry, not enough ingredients to make latte.")
        elif coffee_type == "cappuccino":
            if self.water >= 120 and self.coffee_beans >= 20 and self.milk >= 100 and self.cups >= 1:
                print("Making cappuccino...")
                self.water -= 120
                self.coffee_beans -= 20
                self.milk -= 100
                self.cups -= 1
                print("Here is your cappuccino! Enjoy!")
            else:
                print("Sorry, not enough ingredients to make cappuccino.")
        else:
            print("We don't make such coffee. Thank you for visiting our place.")

    def refill(self, water, coffee_beans, milk, cups):
        self.water += water
        self.coffee_beans += coffee_beans
        self.milk += milk
        self.cups += cups
        print("Refilled the coffee machine.")

    def display_status(self):
        print(f"Water level: {self.water}ml")
        print(f"Coffee beans level: {self.coffee_beans}g")
        print(f"Milk level: {self.milk}ml")
        print(f"Number of cups available: {self.cups}")

coffee_machine = CoffeeMachine()
coffee_machine.display_status()

while True:
    choice = input("What would you like to have? (espresso/latte/cappuccino/exit): ").lower()
    if choice == 'exit':
        print("Thank you for visiting our place!")
        break
    coffee_machine.make_coffee(choice)
    coffee_machine.display_status()





class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Deposited:", self.amount)
        print("Account balance has been updated:", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available:", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Withdrawn:", self.amount)
            print("Account balance has been updated:", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance:", self.balance)

num_users = int(input("Enter the number of users in the bank: "))
users = []

for i in range(num_users):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    user = Bank(name, age, gender)
    users.append(user)

for user in users:
    print("\nWelcome,", user.name)
    while True:
        choice = input("Choose what you want to: (deposit/withdraw/viewbalance/exit): ").lower()
        if choice == 'exit':
            break
        elif choice == 'deposit':
            amount = float(input("Enter the amount to deposit: "))
            user.deposit(amount)
        elif choice == 'withdraw':
            amount = float(input("Enter the amount to withdraw: "))
            user.withdraw(amount)
        elif choice == 'viewbalance':
            user.view_balance()
        else:
            print("Invalid choice!")




import os
import pickle
import getpass

def load_users():
    if os.path.exists("users"):
        with open("users", "rb") as f:
            return pickle.load(f)
    else:
        return {}

def save_users(users):
    with open("users", "wb") as f:
        pickle.dump(users, f)

def sign_up():
    users = load_users()  # Load existing users
    username = input("Enter username: ")
    password1 = getpass.getpass("Enter password: ")
    password2 = getpass.getpass("Re-enter password: ")
    if password1 != password2:
        print("Passwords do not match")
    else:
        users[username] = password1
        save_users(users)
        print("Sign up successful")

def login():
    users = load_users()  # Load existing users
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful")
        main_menu(username)
    else:
        print("Incorrect username or password")

def main_menu(username):
    while True:
        print("\n1: Change password")
        print("2: Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            change_password(username)
        elif choice == "2":
            break
        else:
            print("Please input number 1 or 2.")

def change_password(username):
    users = load_users()  # Load existing users
    old_password = getpass.getpass("Enter old password: ")
    if users[username] == old_password:
        new_password1 = getpass.getpass("Enter new password: ")
        new_password2 = getpass.getpass("Re-enter new password: ")
        if new_password1 != new_password2:
            print("Passwords do not match")
        else:
            users[username] = new_password1
            save_users(users)
            print("Password changed successfully")
    else:
        print("Incorrect password")

if __name__ == "__main__":
    while True:
        print("\n1: Sign up")
        print("2: Login")
        choice = input("Enter your choice: ")
        if choice == "1":
            sign_up()
        elif choice == "2":
            login()
        else:
            print("Please input number 1 or 2.")





import time
import random
name = input("What is your name? ")
print("Hey, " + name + ", It's time to play Hangman with country names!")
print("Let's begin the game:")
time.sleep(1)
print("Start guessing...")
time.sleep(0.5)
countries =[
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia",
    "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
    "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
    "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica",
    "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini",
    "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada",
    "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia",
    "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati",
    "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania",
    "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",
    "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique",
    "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea",
    "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay",
    "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis",
    "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia",
    "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
    "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
    "Syria", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia",
    "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States",
    "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

country = random.choice(countries).lower()

guesses = ''
turns =10
while turns >0:
    failed =0
    for char in country:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed +=1

    print()

    if failed ==0:
        print("You won")
        break

    guess = input("Guess a character: ")[0].lower()
    guesses += guess
    if guess not in country:
        turns -=1
        print("Wrong")

        print("You have", turns, 'more guesses')
        if turns ==0:
            print("You Lose")
            print("The country was:", country.capitalize())
