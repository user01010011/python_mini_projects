import random 

# random.randrange(start,stop) - does not include the stop number, meaning it stops before the stop number, this is the absolute upper bound.
# random.randrange(11) - will start at 0, number generated will be between 0 and 10 (or whatever the number is - 1)
# r = random.randrange(-5, 11) 
# print(r)

# r1 = random.randint(-5, 11) # this will include 11, or whatever the number is
# # random.randint(11) - will generate number between 0 and up to and including 11. 
# print(r1)

top_of_range = input("Type a number: ")
# user input will be returned as strings, like "25", we need to convert it into integer
if top_of_range.isdigit(): 
    top_of_range = int(top_of_range)

    if top_of_range <= 0: 
        print('Please type a number larger than 0 next time.')
        quit()
else: 
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0 

while True: # always true loop (unless break)
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit(): 
        user_guess = int(user_guess)
    else: 
        print('Please type a number next time.')
        continue # automatically brings us back to the top of the loop 

    if user_guess == random_number: 
        print("You got it!")
        break 
    # else:
        # print("You got it wrong!") 
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!") 
 

# print("You got it in " + str(guesses) + " guesses")
# or print statement can convert it for you:
print("You got it in", guesses, "guesses") 