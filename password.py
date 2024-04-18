import pickle
import getpass
#import questionary

p = ''
pc = None
c = 0
fe = False
li = False

try:
    f = open('users.dat', 'rb')
    fe = True
    c = 0
    mde = input("Do you want to login or register: ")
    while mde.lower() not in ['login', 'register']:
        c += 1
        if c > 0:
            print("Invalid input\n")
        mde = input("Do you want to login or register: ")

    if mde.lower() == 'login':
        un = input("Enter username: ")
        p = ''
        while True:
            d = pickle.load(f)
            for i in d.keys():
                if i == un:
                    print(j)
                    p = str(j)
                    li = True
                    
            if li:
                break

        up = getpass.getpass("Enter password(The pass might not be visible but is getting recorded): ")
        if p == up:
            print("Logged in successfully")
            print("Welcom back", un)

        else:
            print("Incorrect password")

    else:
        print("Welcome to registration")
        un = input("Enter username: ")
        e = True
        uns = []
        try:
            while True:
                d = pickle.load(f)
                for i in d.keys():
                    uns.append(i)

        except:           
            f.close()
            
        while un in uns:
            print("Username already exists!")
            un = input("Try another unsername: ")

        pss = getpass.getpass("Enter your password(The pass might not be visible but is getting recorded): ")
        while pc != pss:
            if c >= 1:
                print("Password do not match")
            pc = getpass.getpass("Confirm your password: ")
            print('\n')
            c += 1
        f = open("users.dat", 'wb')
        pickle.dump({un:pss}, f)

except:
    if not fe:
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

    else:
        print('Username not found')
f.close()