from AI.open_artificial_intelligence import OpenArtificialIntelligence

assistant = OpenArtificialIntelligence(
    model_name='gpt-4o-mini',
    system_prompt='You are a helpful yet concise assistant that answers in 10 words or less.',
    save_chat_history=False,
    api_key='<REDACTED>'
)

print(assistant)

reply = assistant.respond('Remember the number 5')
print(reply)

reply = assistant.respond('What did I make you remember?')
print(reply)
