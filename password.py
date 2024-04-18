import pickle
import getpass

p = ''
pc = None
c = 0
fe = False
li = False

#checking if the file exist or not using try
try:
    f = open('users.dat', 'rb')

    #creating variables
    fe = True
    c = 0

    #asking if the user wants to login or register
    mde = input("Do you want to login or register: ")
    while mde.lower() not in ['login', 'register']:
        c += 1
        if c > 0:
            print("Invalid input\n")
        mde = input("Do you want to login or register: ")

    if mde.lower() == 'login':
        #asking the user for their username
        un = input("Enter username: ")
        p = ''


        #checking if the username exist
        while True:
            d = pickle.load(f)
            for i in d.keys():
                if i == un:
                    print(j)
                    p = str(j)
                    li = True
                    
            if li:
                break

        #asking the username for password and verifying if it is correct
        up = getpass.getpass("Enter password(The pass might not be visible but is getting recorded): ")
        if p == up:
            print("Logged in successfully")
            print("Welcom back", un)

        else:
            print("Incorrect password")

    else:
        print("Welcome to registration")

        #asking the user for username
        un = input("Enter username: ")

        #appending all the existing usernames into a list
        uns = []
        try:
            while True:
                d = pickle.load(f)
                for i in d.keys():
                    uns.append(i)

        except:           
            f.close()
            
        #checking if there is another user with same username
        while un in uns:
            print("Username already exists!")
            un = input("Try another unsername: ")

        #asking for the password and also asking to confirm it
        pss = getpass.getpass("Enter your password(The pass might not be visible but is getting recorded): ")
        while pc != pss:
            if c >= 1:
                print("Password do not match")
            pc = getpass.getpass("Confirm your password: ")
            print('\n')
            c += 1

        #writing the data in users.dat file
        f = open("users.dat", 'ab')
        pickle.dump({un:pss}, f)

except:
    if not fe:
        #making the user to register since the file is just being created
        f = open('users.dat', 'wb')
        print("Welcome to registration\n")
        un = input("Enter your user name: ")
        p = getpass.getpass("Enter your password(The pass might not be visible but is getting recorded): ")
        while pc != p:
            if c >= 1:
                print("Password do not match")
            pc = getpass.getpass("Confirm your password: ")
            print('\n')
            c += 1
            

        d = {un:p}
        pickle.dump(d, f)
        print("Registration successful!")

    #if no username exist as specified in login, this statement is executed
    else:
        print('Username not found')

#file is closed
f.close()