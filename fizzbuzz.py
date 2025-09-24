def fizz_buzz(number):                             # We define the function fizz_buzz. The function expects an input
    if number % 3 == 0 and number % 5 == 0:        # If the number is divisible by 3 and 5,
        return "FizzBuzz!!"                        # It returns "FizzBuzz"
    if number % 5 == 0:                            # If the number is divisible by 5,
        return "Buzz"                              # It returns "Buzz"
    if number % 3 == 0:                            # If the number is divisible by 3,
        return "Fizz"                              # It returns "Fizz"
    return f"Try again: {number} "                 # If it is none of the previous cases, it returns the input


print("")
name = input("Hello, please enter your name to continue: ")
print("------------------------------------")
print(f"Welcome, {name} to the FizzBuzz Mystery!")
print("------------------------------------")
print("Type 'break' to exit the game\n")
print("")

while True:                                         # Here we are running a while loop
    user_input = input("Enter your suspect number (or 'break' to exit): ") # The user enters the preferred input
    
    if user_input.lower() == 'break':               # If the input is 'break'
        print(f"Case closed! Good bye {name} and have a good day.") 
        break                                       # We break the loop
    
    try:
        number = int(user_input)                    # We create a variable number that = the user input
        result = fizz_buzz(number)                  # We create another variable called result that stores the number entered by the user.
        print(f"The evidence says: {result}")       # We print the result
    except ValueError:
        print("Invalid clue! Please enter a number or 'break'\n") # If it is not a number, we return an error