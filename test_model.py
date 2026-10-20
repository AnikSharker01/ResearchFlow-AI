
import os
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
model = os.getenv(
    "OPENROUTER_MODEL",
    "nvidia/nemotron-3-ultra:free",
)

if not api_key:
    raise ValueError(
        "OPENROUTER_API_KEY is missing from .env"
    )

print("Testing OpenRouter connection...")

response = completion(
    model=f"openrouter/{model}",
    messages=[
        {
            "role": "user",
            "content": "Reply: ResearchFlow AI connected successfully."
        }
    ],
    api_key=api_key,
    api_base="https://openrouter.ai/api/v1",
    max_tokens=100,
)

print("\nModel response:")
print(response.choices[0].message.content)
