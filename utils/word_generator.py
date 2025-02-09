from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="",
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