from pydantic import BaseModel
from google.genai.types import Content, Part

class GeminiPrompt(BaseModel):
    prompt: str
    system_instruction: str


class ChatHistory(BaseModel):
    chat_history: list[Content]
    
    def to_simple_format(self):
        """
        Convert the chat history to a simple format with role and content keys.
        
        Returns:
            list: A list of dictionaries with 'role' and 'content' keys.
        """
        simple_format = []
        for content in self.chat_history:
            # Extract the text from the first part
            text = content.parts[0].text if content.parts else ""
            simple_format.append({
                "role": content.role,
                "content": text
            })
        return simple_format
    
    @classmethod
    def from_simple_format(cls, simple_format):
        """
        Create a ChatHistory object from a simple format with role and content keys.
        
        Args:
            simple_format (list): A list of dictionaries with 'role' and 'content' keys.
            
        Returns:
            ChatHistory: A ChatHistory object with the converted chat history.
        """
        chat_history = []
        for message in simple_format:
            chat_history.append(
                Content(
                    role=message["role"],
                    parts=[Part.from_text(text=message["content"])]
                )
            )
        return cls(chat_history=chat_history)
