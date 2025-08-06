def chatbot():
    print("Welcome to the Basic Chatbot!")
    print("Type something (type 'bye' to exit):")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi"]:
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I don't understand that.")

chatbot()
