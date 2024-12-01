from dotenv import load_dotenv
import os 
from openai import OpenAI


def get_mp3_details(description):
    load_dotenv('.env')

    api_key = os.getenv('chat_gpt')

    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
       messages = [
                        {"role": "system", "content": "Respond with a single JSON array."},
                        {
                            "role": "user",
                            "content": (
                                f"Given the following YouTube title, provide a JSON object containing the fields: "
                                f'"artist", "album", and "song". Ensure that each field has a non-empty value. '
                                f'Here is the title: "{description}"'
                            ),
                        },
                    ]
    )
    return(completion.choices[0].message.content)



