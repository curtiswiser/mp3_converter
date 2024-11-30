from dotenv import load_dotenv
import os 
from openai import OpenAI

load_dotenv('.env')

api_key = os.getenv('chat_gpt')

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": """
        You are an assistant summarizing articles. Your goal is to extract only factual, relevant information."""},
        {"role": "user", "content": f"what is the capital of france?"}
    ]
)

print(completion.choices[0].message.content)