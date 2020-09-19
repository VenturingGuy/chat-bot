from random import choice

def get_bot_response(user_response):
  bot_response_happy = ["Good job!", "Well done.", "Keep it up."]
  bot_response_disappointed = ["Do better next time.", "I know you can do better than this.", "Good effort, but try harder next time."]

  if user_response == "good":
    return choice(bot_response_happy)
  elif user_response == "bad":
    return choice(bot_response_disappointed)
  else:
    return "I... see. Come back any time. I'm here for you."

print("Welcome back. It's been a while, hasn't it?")
print("So, how have you been doing? Is your work going well? You feel [good] or [bad] about it?")

user_response = ""

while True:
  user_response = input("Well... How DO I feel about my progress today? ")

  if user_response == "good-bye":
    break

  bot_response = get_bot_response(user_response)
  print(bot_response)