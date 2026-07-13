from groq import Groq
client=Groq(api_key="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")
def ask_llm(messages):
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    return response.choices[0].message.content