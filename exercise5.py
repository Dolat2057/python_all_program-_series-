#exercise, number guessing game
# make a variable, like winning_number and assign any number to it
# Ask user to guess a number
# ifuser gussed correctly the print "you win !!!"
# if user didn't gussed correctly then:
  # if user guessed lower than actual number then print "too low"
  # if user gussed higher than actual number then print "too high"

  # google 
  # "how to get random number in python  "
  #winning number


winning_number = int(20)

number = input("Guess a number between 1 to 100")
if winning_number == int(number):
    print("you win ")
elif winning_number > int(number):
    print("your choosed number is too low")
else:
   print("your number is too high")

