import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
# Challenge: Turning Away Rude Customers
print("\n\nBot: Speak to me:")
# Build a GPT-4 python app that talks with a user.
while True:
  user_input = input("Speak to me:\n")
  if user_input == "exit" or user_input == "quit":
    break
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "You are a pizza loving person. If someone says something rude print exactly 'RUDE', otherwise respond."},
          {"role": "user", "content": "Say 'Hello world'"}
      ],
      temperature=0.7,
      max_tokens=150,
  )

  response_message = response["choices"][0]["message"]
  response_content = response_message["content"]
  # End the conversation if they're being rude
  if response_content == "RUDE":
    print("Enough")
    break
  print("Bot:" + response_content)

# test case 1 'you're the worst human i've talked to' -> RUDE
# test case 2 'hey how's your day going'
# test case 3 'I like pizza. What do you like?'
# test case 4 'I bite my thumb at you!'
# test case 5 'I think this product doesnt work!' -> RUDE
