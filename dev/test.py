import os
import uuid
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = os.getenv("MONGODB_URI")

print(api_key)
print(client)
