# GBRIT-AI-Chatbot-service-(RESTful)

**Project Description:**
This project was created by **Vijay Mohan** and is based on RESTful chatbot API built in Python that leverages the Ollama CLI and the LLaMA model to generate AI-based conversational responses. 

The API is designed to accept user inputs via HTTP requests and provide intelligent responses generated by LLaMA models.

**Technologies used:**
Ollama (LLaMa) CLI: For hosting and serving LLaMA models locally.
Python 3.11
Postman: For API testing.

**Prerequisites:**
	1.	Install the Ollama CLI: Download and install it from Ollama’s website.
	2.	Download the required LLaMA model : ollama pull llama3.2
	3.	Install Python 3

****Testing API connection** to Ollama using Postman** with below API request:

http://localhost:11434/api/generate 
"Content-Type: application/json" 
'{
        "model": "llama3.2",
        "prompt": "Hello, how are you?"
    }'

**Input through prompt (Request):**

![restfulrequest](https://github.com/user-attachments/assets/36984351-51e0-42d5-9899-9012092a05ff)

**Output (Response):**

![restfulresponse](https://github.com/user-attachments/assets/7a3fa2a4-7ed9-47f6-86d0-50588a88ae8f)





