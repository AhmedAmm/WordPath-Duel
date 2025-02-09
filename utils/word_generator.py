from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

def generate_words(num_words):
    prompt = f"Generate exactly {num_words} different words, each with exactly 3 letters, separated by spaces."
    completion = client.chat.completions.create(
        model="google/gemini-2.0-flash-lite-preview-02-05:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    words = completion.choices[0].message.content.strip().split()
    print(words)
    return words