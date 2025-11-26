import lmstudio as lms

# Requesting text completion
model = lms.llm()
completion = model.complete("Once upon a time,")
print(completion)

# Requesting a chat response
chat = lms.Chat("You are a helpful shopkeeper assisting a foreign traveller")
chat_response = chat.predict("My hovercraft is full of eels!")
print(chat_response)
