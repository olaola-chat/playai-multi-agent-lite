from pydantic import BaseModel
from enum import Enum


class ModelName():
    GEMINI_2_0_FLASH_LITE = "gemini-2.0-flash-lite"
    GEMINI_2_0_FLASH = "gemini-2.0-flash"


class GeminiModelConfig(BaseModel):
    model: str
    temperature: float
    top_p: float
    max_tokens: int