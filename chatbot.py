from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('MyBot')

# Train the chatbot using the corpus data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Define a function to handle user input and generate responses
def get_response(user_input):
    response = chatbot.get_response(user_input)
    return response.text

# Define a function to start the chatbot
def start_chatbot():
    print('Chatbot started. Type "exit" to quit.')
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            break
        response = get_response(user_input)
        print('Bot: ' + response)

# Start the chatbot
start_chatbot()
