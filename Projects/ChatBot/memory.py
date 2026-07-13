def add_memory(messages,role,content):
    messages.append({
        "role":role,
        "content": content
    })
    return messages