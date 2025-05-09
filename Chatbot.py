def shopping_chatbot():
    print(" Welcome to ShopEasy Chatbot!")
    print("I can help you with: order status, returns, delivery info, and payment methods.")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if "exit" in user_input:
            print("Chatbot: Thank you for shopping with ShopEasy. Have a great day!")
            break
        elif "order" in user_input or "status" in user_input:
            print("Chatbot: You can check your order status in the 'My Orders' section of your account.")
        elif "return" in user_input or "refund" in user_input:
            print("Chatbot: You can request a return or refund within 7 days of delivery.")
        elif "delivery" in user_input:
            print("Chatbot: Delivery usually takes 3-5 business days.")
        elif "payment" in user_input:
            print("Chatbot: We accept credit/debit cards, UPI, and net banking.")
        elif "help" in user_input:
            print("Chatbot: I can help you with order status, returns, delivery, and payment options.")
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Please try asking something else.")

# Run the chatbot
shopping_chatbot()
