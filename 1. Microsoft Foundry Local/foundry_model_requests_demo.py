import requests
import json
from foundry_local import FoundryLocalManager

# Specify the model alias
# alias = "phi-4"
# alias = "Phi-3.5-mini-instruct-cuda-gpu:1"
alias = "mistralai-Mistral-7B-Instruct-v0-2-cuda-gpu:1"

# Create a FoundryLocalManager instance to start the Foundry Local service and load the model
manager = FoundryLocalManager(alias)

# Get the endpoint and model ID
endpoint = manager.endpoint
model_id = manager.get_model_info(alias).id

print(f"✅ Foundry Local running at {endpoint}")
print(f"✅ Model ID: {model_id}")

# Prepare the request payload
payload = {
    "model": model_id,
    "messages": [{"role": "user", "content": "What is the golden ratio?"}]
}

# Send the request to the Foundry Local service
response = requests.post(
    f"{endpoint}/chat/completions",
    headers={"Content-Type": "application/json"},
    data=json.dumps(payload)
)

# Print the response
print(response.json()["choices"][0]["message"]["content"])