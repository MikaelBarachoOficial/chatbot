import re
import random

rules = {
    r"oi|olá|ei": ["Olá! Como posso ajudar?", "Oi! Tudo bem?", "E aí!"],

    r"qual (é|o) seu nome": ["Eu sou um chatbot simples, ainda não tenho um nome!", "Pode me chamar de Assistente Virtual."],

    r"como você está|tudo bem": ["Estou funcionando perfeitamente, obrigado por perguntar!", "Tudo ótimo por aqui!"],

    r"ajuda": ["Claro! Me diga o que você precisa.", "Estou aqui para ajudar. Qual é a sua dúvida?"],

    r"adeus|tchau": ["Até logo!", "Tchau! Volte sempre que precisar."],

    "default": ["Desculpe, não entendi. Pode reformular a pergunta?", "Não tenho certeza de como responder a isso."] # Write a list of the questions to user
}

def get_response(user_message):
    """
    Takes the user's message and returns a response from the chatbot.
    """
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Check if the user's message matches a pattern (case-insensitive)
        if pattern != "default" and re.search(pattern, user_message.lower()):
            # Return a random choice from the list of responses
            return random.choice(responses)
    
    # If no pattern was found, return the default response
    return random.choice(rules["default"])

# This block allows you to test the chatbot logic directly in the terminal
if __name__ == '__main__':
    print("Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")