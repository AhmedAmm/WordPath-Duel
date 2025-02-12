from openai import OpenAI
from dotenv import load_dotenv

import os
import random

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


def generate_words(num_words, prefix="a"):
    prompt = f"""Generate exactly {num_words} different words.
Each word must:
1. Start with the prefix '{prefix}'.
2. Increase in length by exactly one letter each time.
3. Use only lowercase letters.
4. Be separated by spaces.
Example for 6 words with prefix 'a': a ab abc abcd abcde abcdef"""

    try:
        
        completion = client.chat.completions.create(
            model="google/gemini-2.0-flash-lite-preview-02-05:free",
            messages=[{"role": "user", "content": prompt}]
        )

        words = completion.choices[0].message.content.strip().split()

        # Assign balanced positive and negative scores
        scores = []
        for _ in range(num_words // 2):
            scores.append(random.randint(1, 10))   # Positive
            scores.append(random.randint(-10, -1)) # Negative
    
        if num_words % 2 != 0:  # If odd, add one more score
            scores.append(random.choice([-1, 1]))

        random.shuffle(scores)  # Shuffle scores

        # Create the list of tuples (word, score)
        word_tuples = list(zip(words, scores))
    
        return word_tuples
    except Exception as e:
        print("Error generating words: {e}")
        return []
        