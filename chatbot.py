def chatbot():
    print("="*40)
    print("🤖  Welcome to ChatBot 1.0")
    print("="*40)

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello"]:
            print("Bot: Hello! How can I help you today?")
        elif user_input in ["how are you", "how are you doing"]:
            print("Bot: I'm doing great! Thanks for asking.")
        elif user_input in ["what is your name", "who are you"]:
            print("Bot: I'm CodeAlphaBot, your virtual assistant 🤖")
        elif user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a great day! 👋")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot()
