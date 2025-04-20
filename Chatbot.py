from openai import OpenAI
import os


api_key = os.getenv("api_key")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key
)


# Initialize chat history
chat_history = []  
personas ={
    "default": "you are a helpful AI Assistant",
    "sarcastic" : "You are a sarcastic AI who gives witty and mocking answers",
    "poet" : "You are a poet AI that responds in rythmes and verses",

}

print("choose a persona : (default/sarcastic/poet)")

user_persona_input = input("enter persona :").strip().lower()

#persona = personas.get(user_persona_input)

chat_history.append({
    "role": "system",
    "content": personas[user_persona_input]
})


while True:

    user_input = input("Enter Your Prompt:")

    chat_history.append({
      "role": "user",
      "content": user_input
        
    })

    if user_input == "exit":
        break

    completion = client.chat.completions.create(
  
    model="deepseek/deepseek-r1-zero:free",
    messages= chat_history
    )

    response =completion.choices[0].message.content
    print(response)

    chat_history.append({
      "role": "user",
      "content": response
    })
