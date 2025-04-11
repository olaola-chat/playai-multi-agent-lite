from pydantic import BaseModel
from google.genai.types import Content

class GeminiPrompt(BaseModel):
    prompt: str
    system_instruction: str


class ChatHistory(BaseModel):
    chat_history: list[Content]
