from random import choice

''' 
The main meat and potatoes of this program. get_bot_response is set up to take the user's input as 
an argument, and respond accordingly based on its "mood". Currently, there are two "moods" available, 
being happy and disappointed, of which there are three random responses the bot could have.

In the case that the bot doesn't know what to say to your input, it'll give you a consolation of sorts 
as a message instead.
'''

def get_bot_response(user_response):
  bot_response_happy = ["Good job!", "Well done.", "Keep it up."]
  bot_response_disappointed = ["Do better next time.", "I know you can do better than this.", "Good effort, but try harder next time."]

  if user_response == "good":
    return choice(bot_response_happy)
  elif user_response == "bad":
    return choice(bot_response_disappointed)
  else:
    return "I... see? Well, come back any time. I'm here for you."

# This is how the program begins on the user's end, hinting at how they should respond to the bot's prompt.

print("Welcome back. It's been a while, hasn't it?")
print("So, how have you been doing? Is your work going well? You feel [good] or [bad] about it?")

'''
The input is initialized and the user is prompted to enter their response until they say good-bye.
Until the user says good-bye, they'll keep being asked how they feel, calling the get_bot_response 
and having a corresponding response printed out for them.
'''

user_response = ""

while True:
  user_response = input("(Well... How DO I feel about my progress today?) ")

  if user_response == "good-bye":
    break

  bot_response = get_bot_response(user_response)
  print(bot_response)