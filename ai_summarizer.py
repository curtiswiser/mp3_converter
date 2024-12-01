from dotenv import load_dotenv
import os 
from openai import OpenAI


def get_mp3_details(description):
    load_dotenv('.env')

    api_key = os.getenv('chat_gpt')

    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Return JSON array"},
            {"role": "user", "content": f"given this youtube title can you give me JSON results of the artist, album and song: {description}"}
        ]
    )
    return(completion.choices[0].message.content)



