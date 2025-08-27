from openai import OpenAI

client = OpenAI(api_key="SUA_API_KEY")

def conversar(msg):
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": msg}
        ]
    )
    return resposta.choices[0].message.content

while True:
    mens_user = input("Você: ")
    if mens_user.lower() in ["sair", "exit"]:
        break
    resposta = conversar(mens_user)
    print("ChatGPT:", resposta)
