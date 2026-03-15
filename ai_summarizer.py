from groq import Groq

API_KEY = "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"

client = Groq(api_key=API_KEY)

def summarize_note(note_text):

    prompt = f"Summarize this note:\n{note_text}"

    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama-3.1-8b-instant"
    )

    return response.choices[0].message.content