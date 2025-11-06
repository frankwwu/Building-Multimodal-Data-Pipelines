# Microsoft Foundry Local

Microsoft Foundry Local enables you to run AI models locally on your machine. Follow the steps below to install, discover, and use models.

## 1. Install Microsoft Foundry Local

* **Windows**: 
   ```
   winget install Microsoft.FoundryLocal
   ``` 
* **macOS**: 
   ```
   brew tap microsoft/foundrylocal
   brew install foundrylocal
   ```

> **Note:** On macOS, ensure Homebrew is installed first.

## 2. List Available Models

View all models that can be run locally:
   ```
   foundry model list
   ```

For detailed help:
   ```
   foundry model --help
   ```

## 3. Run a Model

Start a model (e.g., `phi-4`) interactively:
   ```
   foundry model run phi-4
   ```
   
## 4. Use the Model in Python

1. **Install the SDK**
   ```
   pip install foundry-local-sdk
   ```

2. **Example: Query the model using requests**
   ``` 
   python foundry_model_requests_demo.py
   ```

3. **Example: Query the model using OpenAI interface**
   ```
   python foundry_model_openai_demo.py
   ```

## References

- **Official Docs**: [Get started with Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started)
- **GitHub Repository**: [microsoft/Foundry-Local](https://github.com/microsoft/Foundry-Local)
