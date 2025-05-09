# Elementary Chatbot for Customer Interaction

# A dictionary mapping keywords (or phrases) to responses.
responses = {
    "hello": "Hi there, how can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm a bot, but I'm here and ready to assist you!",
    "what are your hours": "Our hours are Monday to Friday, 9 AM to 5 PM.",
    "hours": "We're open Monday through Friday from 9 AM to 5 PM.",
    "location": "We are located at 1234 Main Street, Anytown, USA.",
    "price": "For pricing details, please visit our website or contact support.",
    "help": "I'm here to help! What do you need assistance with?",
    "thank you": "You're welcome! Is there anything else I can help with?",
    "bye": "Goodbye! Have a great day!"
}

def get_response(user_input):
    """
    This function checks the user's message against our list of keywords
    and returns an appropriate response. If no keyword is found, it returns
    a default message.
    """
    # Convert the input to lowercase for simpler matching.
    user_input = user_input.lower()
    
    # Check if the user's input contains any of the keywords.
    for key in responses:
        if key in user_input:
            return responses[key]
    
    # If no keywords were matched, return a default response.
    return "I'm sorry, I didn't understand that. Could you please rephrase?"

def run_chatbot():
    """
    Runs a simple loop for interacting with the chatbot via the command line.
    Type 'exit' or 'quit' to end the conversation.
    """
    print("Chatbot: Hello! I'm your assistant. How can I help you today?")
    
    while True:
        # Get input from the user.
        user_input = input("You: ")
        
        # End the conversation if the user types 'exit' or 'quit'.
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get and print the chatbot response.
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "_main_":
    run_chatbot()