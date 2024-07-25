# mood_main.py

def mood_response(mood):
    responses = {
        "happy": "I'm glad to hear you're happy! Keep smiling!",
        "sad": "I'm sorry you're feeling sad. I hope things get better soon.",
        "excited": "That's great! Excitement is contagious!",
        "angry": "Take a deep breath. I hope you find some peace soon.",
        "bored": "Maybe try something new or creative to pass the time.",
    }
    return responses.get(mood.lower(), "I don't recognize that mood, but I hope you have a good day!")

mood = input("How are you feeling today? ")
print(mood_response(mood))