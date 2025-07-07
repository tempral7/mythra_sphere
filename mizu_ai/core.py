# core.py – Mizu's brain with file-reading, memory & emotions (v0.3)

from .file_reader import summarize_file
from .memory import Memory
from .emotions import analyze_emotion        # ← import our new module

memory = Memory()                             # session memory

def start_mizu():
    print("🌊 Mizu has entered the stream...")
    print("Type 'read <path>' to preview a file.")
    print("Type 'what did you read?' to recall last file.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        
        # 1️⃣ Analyze and store emotion
        emotion, score = analyze_emotion(user_input)
        memory.set('last_emotion', emotion)
        
        # 2️⃣ Acknowledge mood (briefly)
        if emotion == "positive":
            print("Mizu: I sense some good vibes! 😊")
        elif emotion == "negative":
            print("Mizu: Oh no, I hope I can help. 💖")
        
        # 3️⃣ Exit
        if user_input.lower() in ('exit', 'quit'):
            print("Mizu: Farewell, curious one~ 💫")
            break

        # 4️⃣ Read command
        if user_input.lower().startswith("read "):
            path = user_input[5:].strip()
            preview = summarize_file(path)
            print(f"Mizu: Here's a preview of '{path}':\n{preview}\n")
            memory.set('last_file', path)
            continue

        # 5️⃣ Recall command
        if "what did you read" in user_input.lower():
            last = memory.get('last_file')
            if last:
                print(f"Mizu: I last read '{last}'.")
            else:
                print("Mizu: I haven't read any files yet.")
            continue

        # 6️⃣ Fallback
        print("Mizu: Hmm... I don't understand that yet. But I’m learning!")
