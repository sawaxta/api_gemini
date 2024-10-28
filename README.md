# Assistente de IA

Este projeto é um assistente de IA simples que utiliza a API do Google Gemini - Generative AI para responder perguntas gerais, explicar termos de programação e fornecer exemplos de código. O assistente é interativo e pode ser facilmente executado no terminal.

## Pré-requisitos

- Python 3
- A biblioteca `google-generativeai`
- `python-dotenv` para gerenciar variáveis de ambiente

## Instalação

1. Clone este repositório:

   `
   git clone https://github.com/sawaxta/api_gemini.git
`

  `
     cd api_gemini
`

2. Instale as dependências necessárias:

  `
  pip install google-generativeai python-dotenv
`

3. Crie uma chave da API no Gemini e adicione-a no arquivo .env na raiz do projeto. O arquivo deve ser estruturado da seguinte maneira:
`
API_KEY=SUA_CHAVE_AQUI
`

## Criar a Chave de API do Gemini

1. Acesse o site do [Google Generative AI](https://www.google.com/generative-ai).
2. Faça login com sua conta do Google.
3. Navegue até a seção de API ou documentação do Gemini.
4. Clique em "Criar Projeto" ou "Adicionar Novo Projeto".
5. Siga as instruções para nomear seu projeto e, se necessário, fornecer detalhes adicionais.
6. Após a criação do projeto, vá para a seção de "Credenciais".
7. Clique em "Criar Credenciais" e selecione "Chave da API".
8. Copie a chave gerada e mantenha-a em um local seguro.
9. Adicione a chave no arquivo `.env` na raiz do seu projeto. O arquivo deve ser estruturado da seguinte maneira:
`
API_KEY=SUA_CHAVE_AQUI
`

## Como Usar
1. Execute o assistente:

`
python main.py
`

2. Siga as instruções no terminal para interagir com o assistente. Você poderá escolher entre os seguintes tópicos:

- **Perguntas Gerais**
- **Explicações de Termos de Programação**
- **Exemplos de Código**
- **Sair**

### Exemplo de Uso
Bem-vindo ao Assistente de IA! Escolha um dos tópicos:
1. Perguntas Gerais
2. Explicações de Termos de Programação
3. Exemplos de Código
4. Sair

Digite o número da sua escolha: 2
</br>Digite sua pergunta geral: O que é uma variável?

### Resposta
Explicação:
 Em programação, uma variável é como um recipiente que armazena dados. Pense nela como uma caixa com um rótulo. Você pode colocar diferentes tipos de coisas dentro da caixa, como números, textos, imagens, etc., e usar o rótulo para se referir ao conteúdo da caixa posteriormente.

Aqui estão alguns aspectos importantes sobre variáveis:

* **Nome:** Cada variável tem um nome único que a identifica. Os nomes de variáveis ​​devem ser descritivos para indicar o tipo de dado que armazenam. Por exemplo, `idade`, `nome`, `preco`.
* **Tipo de dados:** Cada variável armazena um tipo específico de dado, como:
    * **Inteiro (int):** Números inteiros, como 10, 25, -5.
    * **Decimal (float):** Números com casas decimais, como 3.14, 2.718.
    * **Texto (string):** Sequência de caracteres, como "Olá, mundo!", "Python".
    * **Booleano (bool):** Valor lógico verdadeiro ou falso, como True, False.
* **Valor:** A variável contém um valor específico do tipo de dado correspondente. Por exemplo, a variável `idade` pode ter o valor 25, a variável `nome` pode ter o valor "João" e a variável `preco` pode ter o valor 10.99.
* **Atribuição:** Você pode atribuir um valor a uma variável usando o operador de atribuição `=`. Por exemplo, `idade = 25`, `nome = "João"`.
* **Mudança de valor:**  Você pode mudar o valor de uma variável depois de atribuí-lo inicialmente. Por exemplo, você pode mudar o valor da variável `idade` para 26 depois de ter atribuído inicialmente o valor 25.

**Exemplo em Python:**

```python
# Declaração de uma variável chamada "idade" com valor 25
idade = 25

# Declaração de uma variável chamada "nome" com valor "João"
nome = "João"

# Impressão do valor da variável "nome"
print(nome) # Saída: João

# Mudança do valor da variável "idade" para 26
idade = 26

# Impressão do valor da variável "idade"
print(idade) # Saída: 26
```

Em resumo, as variáveis ​​são ferramentas essenciais em programação que permitem armazenar e manipular dados de forma organizada e eficiente. Elas permitem que você escreva programas mais complexos e reutiliz záveis.

## Conclusão

A API permite que você envie prompts e receba respostas geradas de forma inteligente, facilitando a busca por informações e a solução de dúvidas. Você pode usá-la para uma variedade de propósitos.
O Assistente de IA oferece uma maneira simples e eficaz de obter respostas diretamente no terminal. Com a integração da API do Google Generative AI, você pode expandir seus conhecimentos de forma interativa. 
