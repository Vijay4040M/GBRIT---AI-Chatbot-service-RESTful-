import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
import json
from fastapi.responses import StreamingResponse

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class RequestModel(BaseModel):
    model: str
    prompt: str

@app.post("/api/generate")
async def generate_response(request: RequestModel):
    prompt = request.prompt
    
    logger.info(f"Received prompt: {prompt}")
    
    def generate_chunks():
        response = ""  # Initialize the response variable here
        
        try:
            for word in prompt.split():
                response += word + " "
                time.sleep(0.1)  # Simulate a delay like streaming response
                yield json.dumps({
                    "model": request.model,
                    "response": response.strip(),
                    "done": False
                }) + "\n"
            
            logger.info("Streaming completed.")
            yield json.dumps({
                "model": request.model,
                "response": response.strip(),
                "done": True
            }) + "\n"
        except asyncio.CancelledError:
            logger.warning("Streaming was cancelled by the client.")
            raise HTTPException(status_code=499, detail="Client Closed Request")
    
    return StreamingResponse(generate_chunks(), media_type="application/json")
