from dotenv import load_dotenv
import os 
from openai import OpenAI
import json 



def convert_to_json(data):
    data = data.replace('`', '')
    data = data.replace('json', '')
    data = data.replace('[', '')
    data = data.replace(']', '')
    data = data.strip()
    return json.loads(data)

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

    #doesn't return a full JSON array so created a cheater function 
    return convert_to_json(completion.choices[0].message.content)


