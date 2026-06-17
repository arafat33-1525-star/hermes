"""
Hermes Agent - FastAPI Application
"""

from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Hermes Agent",
    description="Hermes AI Agent API",
    version="1.0.0"
)

# Data models
class Message(BaseModel):
    text: str

class Response(BaseModel):
    status: str
    message: str

# Health check endpoint
@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "hermes-agent",
        "version": "1.0.0"
    }

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Hermes Agent API",
        "status": "running",
        "docs": "/docs",
        "health": "/health"
    }

# Agent endpoint
@app.post("/agent")
async def agent(message: Message):
    """Process message through Hermes agent"""
    return {
        "status": "success",
        "input": message.text,
        "output": f"Hermes processed: {message.text}",
        "agent": "hermes"
    }

# Status endpoint
@app.get("/status")
async def status():
    """Get agent status"""
    return {
        "agent": "hermes",
        "status": "active",
        "port": os.getenv("PORT", "8000"),
        "log_level": os.getenv("LOG_LEVEL", "INFO")
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)