import os
from openai import OpenAI

os.environ["OPENAI_API_BASE"] = "http://127.0.0.1:5000/v1"
os.environ["OPENAI_API_KEY"] = "suchkey"
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
        {
            "role": "assistant",
            "content": "such a nice test",
        },
{
            "role": "user",
            "content": "repeat what you said, word by word",
        },
    ],

    model="gpt3"
)

print(chat_completion.choices[0].message)