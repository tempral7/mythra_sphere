def start_mizu():
    print("🌊 Mizu has entered the stream...")
    print("Hello! I'm Mizu, your mysterious assistant!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Mizu: Farewell, curious one~ 💫")
            break
        else:
            print("Mizu: Hmm... I don't understand that yet. But I’m learning!")