import random

def magic_8_ball():
    # List of possible responses the Magic 8 Ball can give.
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
        "As I see it, yes... but I wouldn't bet on it.",
        "Ask again later, I'm watching my shows.",
        "Better not tell you now, it's a secret.",
        "Cannot predict now, I'm too lazy.",
        "Concentrate and ask again, I wasn't listening.",
        "Don’t count on it, unless you count backwards.",
        "It is certain, as certain as coffee in the morning.",
        "It is decidedly so, and by 'it', I mean 'maybe'.",
        "Most likely, but don't quote me on that.",
        "My reply is no, but I've been wrong before.",
        "My sources say no, but they're unreliable.",
        "Outlook not so good, just like my internet connection.",
        "Outlook good, like a sunny day in a British summer.",
        "Reply hazy, try again after I've had my coffee.",
        "Signs point to yes, but they're not very good signs.",
        "Very doubtful, like my decision-making skills.",
        "Yes, definitely, unless it doesn't happen.",
        "Yes, in a parallel universe.",
        "You may rely on it, but I'd get a second opinion.",
        "Enroll at The Tech Academy!",
        "Do a Tech Academy boot camp!"
    ]

    while True:
        # Ask the user to input a question for the Magic 8 Ball.
        question = input("Ask the Magic 8 Ball a question (or type 'exit' to quit): ").strip()
        
        # If the user types 'exit', end the game.
        if question.lower() == 'exit':
            print("Goodbye! Remember, the Magic 8 Ball knows all (sort of).")
            break
        # If the user doesn't input anything, prompt them to ask a question or exit.
        elif not question:
            print("Please ask a question or type 'exit' to quit.")
        # If the user asks a question, display a random response from the list.
        else:
            print(random.choice(responses))

if __name__ == '__main__':
    try:
        magic_8_ball()
    except KeyboardInterrupt:
        # Handle sudden interruptions gracefully.
        print("\nMagic 8 Ball session ended abruptly. Farewell!")
    except Exception as e:
        # Generic error handling to catch unexpected issues.
        print(f"An error occurred: {e}")


