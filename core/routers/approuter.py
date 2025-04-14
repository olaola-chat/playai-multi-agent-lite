from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from fastapi.responses import StreamingResponse
from core.orchestra import AgentOrchestra
from core.config.model_predefine_config import predefine_model_configs


# Create router instance
router = APIRouter(
    prefix="/agents",
    tags=["agents"],
    responses={404: {"description": "Not found"}},
)

# Pydantic models for request/response
class AgentRequest(BaseModel):
    """Model for agent creation request"""
    name: str
    role: str
    capabilities: Optional[List[str]] = None

class AgentResponse(BaseModel):
    """Model for agent response"""
    id: str
    name: str
    role: str
    capabilities: List[str]
    status: str

# New model for multi-agent request
class MultiAgentRequest(BaseModel):
    """Model for multi-agent request"""
    chat_history: str 
    # format [{"role": "user", "content": "user_message"},
    #        {"role": "AI character name", "content": "AI_message"}]

    current_question: str
    


@router.post("/multi-agent")
async def multi_agent_response(request: MultiAgentRequest):
    """
    Get a response from the multi-agent system
    """
    try:
        # Create an instance of AgentOrchestra
        orchestra = AgentOrchestra()
        
        # Call the multi_agent_response method
        response = orchestra.multi_agent_response(
            chat_history=request.chat_history,
            current_question=request.current_question,
            model_configs=predefine_model_configs
        )
        
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")


@router.post("/multi-agent/stream")
async def multi_agent_response_stream(request: MultiAgentRequest):
    """
    Get a streaming response from the multi-agent system
    """
    try:
        # Create an instance of AgentOrchestra
        orchestra = AgentOrchestra()
        
        # Create a generator function that yields chunks from the stream
        async def generate():
            for chunk in orchestra.multi_agent_response_with_stream(
                chat_history=request.chat_history,
                current_question=request.current_question,
                model_configs=predefine_model_configs
            ):
                yield f"data: {chunk}\n\n"
        
        # Return a StreamingResponse
        return StreamingResponse(
            generate(),
            media_type="text/event-stream"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}") 