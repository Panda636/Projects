from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Create and configure the chatbot
chatbot = ChatBot(
    'FriendlyBot',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',   # bonus: can do math!
    ]
)

# -------------------------------
# Quick training with your own conversations
trainer = ListTrainer(chatbot)

trainer.train([
    "Hi", "Hello! How can I help you today?",
    "Hey", "Hey there! 😊 What's up?",
    "How are you?", "I'm doing great, thanks! How about you?",
    "What's your name?", "I'm FriendlyBot, nice to meet you!",
    "Tell me a joke", "Why don't programmers like nature? It has too many bugs! 😂",
    "bye", "See you later! Have a great day 👋",
    "What time is it?", "Sorry, I don't have a clock... but it's always chat time! 🕒",
])

# -------------------------------
# Optional: Train with built-in English corpus (small talk, greetings, etc.)
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train("chatterbot.corpus.english")          # greetings, ai, botprofile, etc.

print("FriendlyBot is ready! Type 'quit' or 'bye' to exit.\n")

while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'bye', 'exit']:
            print("Bot: Goodbye! 👋")
            break

        response = chatbot.get_response(user_input)
        print("Bot:", response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break