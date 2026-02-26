import nltk
patterns = {
"hello": "Hello!",
"hi": "Hi there!",
"how are you?": "I'm doing well, thank you!",
"what's up?": "Not much, how about you?",
"what's your name?": "My name is ChatBot.",
"who are you?": "I'm a chatbot programmed to assist you.",
"where are you from?": "I exist in the digital realm.",
"tell me a joke": "Sure, here it is: Why don't scientists trust atoms? Because they make up everything!",
"how old are you?": "I don't have an age as I am a virtual entity.",
"what is the meaning of life?": "The meaning of life is subjective and can vary for each individual.",
"bye": "Goodbye!",
"see you later": "Until next time!",
"thank you": "You're welcome!",
"sorry": "No problem!",
"I don't know": "That's alright. Is there anything else I can assist you with?",
"can you help me?": "Of course! I'm here to help. What do you need assistance with?",
"what is your favorite color?": "As a chatbot, I don't have preferences like humans do.",
"do you have any hobbies?": "My main focus is on providing helpful responses to your queries.",
"what can you do?": "I can answer questions, provide information, and engage in conversation.",
"how can I contact you?": "You can reach out to me through this chat interface.",
"where can I find more information?": "You can visit our website for more information.",
"can you tell me a fun fact?": "Sure! Did you know that the world's smallest mammal is the bumblebee bat?",
"what is the weather like today?": "I'm sorry, but I don't have real-time weather information.",
}
# Function to match the user input with patterns and generate a response
def get_response(user_input):
  user_input = user_input.lower()
  for pattern, response in patterns.items():
    if pattern in user_input:
      return response
  return "I'm sorry, I don't understand."
# Get user input and generate responses
while True:
  user_input = input("You: ")
  if user_input.lower() in ["exit", "quit"]:
    break
  response = get_response(user_input)
  print("ChatBot:", response)
  if user_input.lower() in ["exit", "quit"]:
    break