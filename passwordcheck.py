# Lets' make a restriction of 10 symbols for password?
while True:
    password = (input("Enter the password (max 10 symbols):\n"))
    if len(password) <= 10: # If it is no longer than 10 symbols, then OK
        print("OK")
        break # Going out of the loop if the password is OK
    else:
        print("The password is too long! Try again, please!") # in other cases we recieve an error
 