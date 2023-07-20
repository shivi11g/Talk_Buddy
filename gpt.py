import openai

openai.api_key = ''
messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]



message = input("User : ")
if message:
    messages.append(
        {"role": "user", "content": message},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

reply = chat.choices[0].message.content
print(f"ChatGPT: {reply}")
messages.append({"role": "assistant", "content": reply})

import openai
openai.api_key = ''

model_engine = "text-davinci-003"
prompt = "Hello how are you?"

completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_token = 1024,
    n1 = 1,
    stop = None, 
    temperature = 0.5,
)

response = completion.choices[0].text 
print(response)

