import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    # Greetings
    [
        r"^(hi|hello|hey|hii)$",
        [
            "Hello! How can I help you today?",
            "Hi there! What would you like to know?"
        ]
    ],

    # Asking name of bot
    [
        r"^what is your name\??$",
        [
            "I am a simple NLTK chatbot created in Python.",
            "You can call me NLTK-Chatbot."
        ]
    ],

    # Asking for creator
    [
        r"^(who created you|who is your developer)\??$",
        [
            "I was created by a Python developer using the NLTK library.",
            "A human developer built me using Python and NLTK."
        ]
    ],

    # College / project related
    [
        r"^what can you do\??$",
        [
            "I can answer simple questions, respond to greetings, and act as a demo NLP chatbot.",
            "I can chat with you, answer basic FAQs, and show how rule-based NLP works."
        ]
    ],

    # Simple FAQ examples
    [
        r"^what is nltk\??$",
        [
            "NLTK is a Natural Language Processing library in Python used for working with human language data."
        ]
    ],
    [
        r"^(what is nlp\??|define nlp)$",
        [
            "NLP stands for Natural Language Processing, a field of AI that helps computers understand human language."
        ]
    ],
    [
        r"^what is a chatbot\??$",
        [
            "A chatbot is a computer program that uses rules or AI to simulate conversation with users."
        ]
    ],

    # Thanks
    [
        r"^(thank you|thanks)$",
        [
            "You are welcome!",
            "Happy to help!",
            "Anytime!"
        ]
    ],

    # Exit patterns
    [
        r"^(quit|exit|bye)$",
        [
            "Goodbye! Have a great day.",
            "Bye! Closing the chatbot now."
        ]
    ],

    # Fallback
    [
        r"(.*)",
        [
            "I am not sure about that. Could you rephrase your question?",
            "I do not have an answer for that yet, but I am learning!"
        ]
    ],
]

def main():
    print("NLTK Chatbot: Hello! Type something to start chatting.")
    print("Type 'bye' or 'quit' to exit.")

    chatbot = Chat(pairs, reflections)

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["bye", "quit", "exit"]:
            print("Chatbot: Goodbye! Have a nice day.")
            break

        response = chatbot.respond(user_input)
        if response:
            print("Chatbot:", response)
        else:
            print("Chatbot: I did not understand that. Please try again.")

if __name__ == "__main__":
    main()

