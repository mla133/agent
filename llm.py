import requests

LLM_URL = "http://localhost:8080/completion"

def build_prompt(messages):
    """
    Convert chat messages into a strict Qwen-compatible prompt
    """

    prompt = ""

    for msg in messages:
        if msg["role"] == "system":
            prompt += f"<|system|>\n{msg['content']}\n"
        elif msg["role"] == "user":
            prompt += f"<|user|>\n{msg['content']}\n"
        elif msg["role"] == "assistant":
            prompt += f"<|assistant|>\n{msg['content']}\n"
        elif msg["role"] == "tool":
            prompt += f"<|tool|>\n{msg['content']}\n"

    prompt += "<|assistant|>\n"

    return prompt


def chat(messages):
    prompt = build_prompt(messages)

    response = requests.post(
        LLM_URL,
        json={
            "prompt": prompt,
            "n_predict": 256,
            "temperature": 0.0,
            "stop": ["<|user|>", "<|assistant|>"]
        },
        timeout=(10, 300)
    )

    data = response.json()

    # Case 1: llama.cpp modern format
    if "content" in data:
        return data["content"]

    # Case 2: OpenAI-style fallback
    if "choices" in data:
        choice = data["choices"][0]
        return choice.get("text", "") or choice.get("message", {}).get("content", "")

    # Case 3: unexpected format
    print("Unknown LLM response format:", data)
    return ""
