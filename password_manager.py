master_pwd = input("What is the master password? ")

def view(): 
    with open('passwords.txt', 'r') as f: 
        for line in f.readlines(): # read all of the lines from the file 
            data = line.rstrip() # strip the character return from the line
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)


def add(): 
    name = input("Account Name: ")
    pwd = input("Password: ")
    # use "with" to automatically close the file once you are done with the operations
    # you can also use: 
        # file = open('passwords.txt', 'a')
        # file.close()
    # 'w' = write mode (will overwrite whatever you had in the file), 
    # 'a' = append mode (add something to the end of that fine, and create a new file if that file does not already exist), 
    # 'r' = read mode only
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")  # go to the next line


while True: 
    mode = input("Would you like to add a new password or view existing ones? (view / add) Enter 'q' to quit: ").lower()
    if mode == "q": 
        break 

    if mode == "view": 
        view()
    elif mode == "add":
        add()
    else: 
        print("Invalid mode.")
        continue 