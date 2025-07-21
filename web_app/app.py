from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os

# Set AWS environment variables
os.environ["AWS_DEFAULT_REGION"] = "us-east-2"

# Import the agent from our local service file
from agent_service import agent

app = FastAPI()

# Enable CORS for Angular development server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    status: str

@app.get("/")
async def root():
    return {"message": "Strands Agent API is running!"}

@app.post("/chat", response_model=ChatResponse)
async def chat_with_agent(request: ChatRequest):
    try:
        # Use the agent synchronously (we'll make it async later if needed)
        result = agent(request.message)
        
        # Extract the text content from the message structure
        if isinstance(result.message, dict) and 'content' in result.message:
            # Handle the case where content is a list of text blocks
            content = result.message['content']
            if isinstance(content, list) and len(content) > 0:
                response_text = content[0].get('text', str(content[0]))
            else:
                response_text = str(content)
        else:
            # Fallback to string conversion
            response_text = str(result.message)
        
        return ChatResponse(
            response=response_text,
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
