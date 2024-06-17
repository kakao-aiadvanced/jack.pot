import ollama

response = ollama.chat(
    model='llama3',
    messages=[{
        "role": "user",
         "content": "what is the Newton’s law?",
    }])

print(response['message']['content'])
