# for cases when the user enters invalid input
while True:
    try:
        Cels = float(input("Enter the Celsius temperature:\n"))
        break # if the input is correct, the user exites the loop
    # create an error handling helping message, while using ValueError (for cases when the code can't handle the input you provided)
    except ValueError:
        print('Invalid input! Try entering a numerical temperature!')
              
Far = (9 / 5) * Cels + 32
print('The temperature of Celsius', Cels, 'is', Far, 'degrees Fahrenheit')