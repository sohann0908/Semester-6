# Import "chatbot" from
# chatterbot package.
from chatterbot import ChatBot

# Inorder to train our bot, we have
# to import a trainer package
# "ChatterBotCorpusTrainer"
from chatterbot.trainers import ChatterBotCorpusTrainer


# Give a name to the chatbot “corona bot”
# and assign a trainer component.
chatbot=ChatBot('corona bot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Now let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
			"chatterbot.corpus.english.conversations" )


question = input("Enter your question bro:(Enter 0 to exit) ")
while question != "0":
        response = chatbot.get_response(question)
        print(response)
        question = input("Enter your question:(Enter No to exit) ")
print("Goodbye")
