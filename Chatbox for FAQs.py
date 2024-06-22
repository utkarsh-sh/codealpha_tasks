import nltk
import re

# Download necessary NLTK packages
nltk.download('punkt')
nltk.download('wordnet')

# Define a list of common phrases and their responses
pairs = [
    [
        r"earbud",
        "Our OnePlus Earbud is ture wireless earbuds deliver crisp clear sound with enhanced bass quality through its 12.4mm driver unit. What would you like to know about it?",
    ],
    [
        r"battery life",
        "The flagship-level battery life delivers 38 hours of non-stop music on a single charge.",
    ],
    [
        r"waterproof",
        "Yes, IP55 Water and Sweat Resistance.",
    ],
    [
        r"warranty",
        "OnePlus provides a 1-year limited warranty.",
    ],
    [
        r"features",
        "Our Earbud has bluetooth version:5.3, Crystal Clear Call, Sound Master Euqalizers.",
    ],
    [r"price", "It costs Rs2500."],
]

# Function to check if a pattern matches the user input
def match_pattern(pattern, user_input):
    return re.search(pattern, ' '.join(user_input)) is not None

# Create a chatbot class
class OnePlusFAQChatbot:
    def __init__(self, pairs):
        self.pairs = pairs

    def greet(self):
        print("Hi! I'm here to answer your questions about our OnePlus Nord 2 Earbud.")

    def chat(self):
        print("Ask me anything about the Earbud!")
        while True:
            user_input = input(">..  ")
            processed_input = self.preprocess(user_input)
            response = self.get_response(processed_input)
            print(response)
            if response == "Goodbye":
                break

    def preprocess(self, sentence):
        # Tokenize the sentence
        tokens = nltk.word_tokenize(sentence)
        # Convert to lowercase
        tokens = [token.lower() for token in tokens]
        return tokens

    def get_response(self, processed_input):
        for (pattern, response) in self.pairs:
            # Check if user input matches a pattern using custom matching
            if match_pattern(pattern, processed_input):
                return response

        # If no match found, return a default message
        return "Sorry, I don't understand. Can you rephrase that?"

# Create an instance of the chatbot
chatbot = OnePlusFAQChatbot(pairs)

# Start the chat with predefined questions
chatbot.greet()
chatbot.chat()