import uvicorn
import argparse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.routers.approuter import router

# Create FastAPI app instance
app = FastAPI(
    title="Player Multi-Agent API",
    description="API for the Player Multi-Agent system",
    version="0.1.0"
)

# # Configure CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # In production, replace with specific origins
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Include routers
app.include_router(router)

# Root endpoint
@app.get("/")
async def root():
    """
    Root endpoint that returns basic API information
    """
    return {
        "message": "Welcome to the Player Multi-Agent API",
        "version": "0.1.0",
        "status": "operational"
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify API status
    """
    return {
        "status": "healthy",
        "service": "multi-agent-api"
    } 
