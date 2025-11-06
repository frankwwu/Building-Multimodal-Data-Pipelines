import json
from openai import OpenAI
from foundry_local import FoundryLocalManager

# Choose model alias
# alias = "phi-4"
# alias = "Phi-3.5-mini-instruct-cuda-gpu:1"
alias = "mistralai-Mistral-7B-Instruct-v0-2-cuda-gpu:1"

# Start Foundry Local and load the model
manager = FoundryLocalManager(alias)

endpoint = manager.endpoint
model_id = manager.get_model_info(alias).id

print(f"✅ Foundry Local running at {endpoint}")
print(f"✅ Model ID: {model_id}")

# Create OpenAI-compatible client
client = OpenAI(
    base_url=endpoint,
    api_key="local"  # Foundry Local doesn’t require this, but SDK expects a key
)

# ---- FIX HERE ----
# Use only user → assistant pattern (no 'system' role)
response = client.chat.completions.create(
    model=model_id,
    messages=[
        {"role": "user", "content": "What is the golden ratio?"}
    ],
    temperature=0.7,
    max_tokens=512
)
# -------------------

# Print response
print("\n🧠 Model Response:")
print(response.choices[0].message.content)
