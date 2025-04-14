from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from core.prompt.gemini_prompt import GeminiPrompt
from core.config.gemini_model_config import GeminiModelConfig

load_dotenv()

def generate_text_with_stream(user_prompt: GeminiPrompt, model_config: GeminiModelConfig):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = model_config.model
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_prompt.prompt),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=model_config.temperature,
        top_p=model_config.top_p,
        max_output_tokens=model_config.max_tokens,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text=user_prompt.system_instruction),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        yield chunk.text


def generate_text(user_prompt: GeminiPrompt, model_config: GeminiModelConfig):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = model_config.model
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_prompt.prompt),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=model_config.temperature,
        top_p=model_config.top_p,
        max_output_tokens=model_config.max_tokens,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text=user_prompt.system_instruction),
        ],
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    return response.text


if __name__ == "__main__":
    for chunk in generate_text_with_stream():
        print(chunk, end="")
