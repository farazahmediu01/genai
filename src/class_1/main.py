from openai import OpenAI
import dotenv
import rich
import os


dotenv.load_dotenv()
GEMENI_API_KEY = os.getenv("GEMENI_API_KEY")

client = OpenAI(api_key=GEMENI_API_KEY,
     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ]
)

response = response.choices[0].message
rich.print(response)