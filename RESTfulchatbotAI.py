import requests
import json

# Define the URL for the Ollama API
OLLAMA_URL = "http://localhost:11434/api/generate"

# Function to send a message to Ollama and get a response
def chat_with_ollama(prompt):
    payload = {
        "model": "llama3.2",
        "prompt": prompt
    }

    try:
        # Use streaming mode to handle multiple JSON chunks
        response = requests.post(OLLAMA_URL, json=payload, stream=True)

        # Check if the request was successful
        if response.status_code == 200:
            full_response = ""
            # Read the response in chunks and process each one
            for chunk in response.iter_lines():
                if chunk:
                    try:
                        # Decode and parse the JSON chunk
                        chunk_data = json.loads(chunk)
                        # Append the chunk's response to the full response
                        full_response += chunk_data.get("response", "")
                        if chunk_data.get("done", False):
                            break  # Stop when the "done" flag is true
                    except json.JSONDecodeError:
                        return "Error: Malformed chunk received from the server."
            
            return full_response if full_response else "No response from model."

        else:
            return f"Error: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"

# Example usage: Get a response for a prompt
if __name__ == "__main__":
    user_prompt = "Give me a list of GenAI tools?"
    response = chat_with_ollama(user_prompt)
    print("Response from Ollama:", response)