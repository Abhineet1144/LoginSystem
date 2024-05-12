import pwinput
import bcrypt
import json

class Main:
    def __init__(self):
        try:
            f = open('users.json', 'r')
        except FileNotFoundError:
            f = open("users.json", "w")
            data = {}
            json.dump(data, f, indent=3)

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)
    
    def user_data(self):
        f1 = open('users.json', 'r')
        self.data = json.load(f1)
        user_detail = {k:v for k,v in self.data.items()}
        return user_detail

    def register(self):
        print("\nWelcome to registration\n")
        self.user_name = input("Enter your user name: ").lower()
        
        user_detail = self.user_data()

        if self.user_name in user_detail:
            print("Username already exists")
            self.user_name = input("Enter your user name: ").lower()

        self.password = pwinput.pwinput(prompt="Enter your password: ", mask="*")
        conform_password = pwinput.pwinput(prompt="Confirm your password: ", mask="*")
        while conform_password != self.password:
            print("Password do not match")
            conform_password = pwinput.pwinput(prompt="Confirm your password: ", mask="*")
            print('\n')
        
        hashed_password = self.hash_password(self.password)
        
        fdata = {self.user_name: {"password": hashed_password.decode()}}
        self.data.update(fdata)
        
        f2 = open('users.json', 'r+')
        json.dump(self.data, f2, indent=3)
        print("Registration successful!")

    def login(self):
        user_detail = self.user_data()
        user_name = input("Enter your user name: ").lower()
        while user_name not in user_detail:
            print("Username does not exist")
            user_name = input("Enter your user name: ").lower()
        hashed_password = user_detail[user_name]["password"].encode()
        
        password = pwinput.pwinput(prompt="Enter your password: ", mask="*")
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            print("Login successful")
        else:
            print("Incorrect password")

obj = Main()
choice = input("Do you want to login or register: ").lower()

while choice not in ['register', 'login']:
    print("Invalid input\n")
    choice = input("Do you want to login or register: ")

if choice == 'register':
    obj.register()

if choice == 'login':
    obj.login()