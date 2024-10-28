import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessa a chave da API armazenada no .env
api_key = os.getenv("API_KEY")

# Configura a API com a chave carregada
genai.configure(api_key=api_key)

# Função que usa o modelo para gerar resposta
def generate_response(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Função principal para gerenciar o assistente
def assistant():
    print("Bem-vindo ao Assistente de IA! Escolha um dos tópicos:")
    print("1. Perguntas Gerais")
    print("2. Explicações de Termos de Programação")
    print("3. Exemplos de Código")
    print("4. Sair")

    while True:
        choice = input("\nDigite o número da sua escolha: ")
        
        if choice == "1":
            question = input("Digite sua pergunta geral: ")
            response = generate_response(question)
            print("\nResposta:\n", response)

        elif choice == "2":
            term = input("Digite o termo de programação que deseja entender: ")
            response = generate_response(f"Explique o termo de programação '{term}'.")
            print("\nExplicação:\n", response)

        elif choice == "3":
            topic = input("Digite um tópico para um exemplo de código (ex: loops, funções): ")
            response = generate_response(f"Mostre um exemplo de código para '{topic}' em Python.")
            print("\nExemplo de Código:\n", response)

        elif choice == "4":
            print("Saindo do Assistente. Até logo!")
            break

        else:
            print("Escolha inválida. Tente novamente.")

# Iniciar o assistente
if __name__ == "__main__":
    assistant()