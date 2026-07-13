from web_agent import search_web
from llm import ask_llm


def decide_agent(messages, prompt):

    keywords = ["news", "latest", "internet", "today"]

    if any(k in prompt.lower() for k in keywords):

        web_data = search_web(prompt)

        messages.append({
            "role": "user",
            "content": f"Answer using this information:\n{web_data}"
        })

        return ask_llm(messages)

    else:

        messages.append({
            "role": "user",
            "content": prompt
        })

        return ask_llm(messages)