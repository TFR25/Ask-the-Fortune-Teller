# COM203
# Parsons, J. J. (2018). New perspectives on computer concepts 2018, comprehensive (20th ed.). Cengage.
# A while-loop that randomly selects an item from a list.
# Program allows player to ask multiple questions.
# A list that holds predicitons.
# Random number generator randomly selects a prediction from list.
# Fortune Teller
import random
predictions = ["yes", "no", "maybe", "certainly", 
              "try again later", "my sources say no", "very doubtful" 
              "not now", "outlook good", "cannot predict now", "most \
              likely", "reply hazy, try again", "signs point to yes"]
print("Welcome to Ask the Fortune Teller.")
print("Ask the Fortune Teller a question.")
question = input()
# Loop that repeats until player types "Quit"
while question.upper() != "QUIT":
  answer = random.choice(predictions)
  print("My answer is: " + answer + ".")
  print("Ask another question or type Quit to end!")
  question = input()



