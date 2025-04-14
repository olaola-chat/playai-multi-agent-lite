from google.genai.types import Content, Part
from core.prompt.gemini_prompt import ChatHistory

def main():
    # Create a sample chat history using the Google Generative AI types
    chat_history = ChatHistory(
        chat_history=[
            Content(
                role="user",
                parts=[
                    Part.from_text(text="hihi")
                ]
            ),
            Content(
                role="model",
                parts=[
                    Part.from_text(text="你好呀")
                ]
            ),
        ]
    )
    
    # Print the original format
    print("Original format:")
    for content in chat_history.chat_history:
        print(f"Role: {content.role}, Text: {content.parts[0].text}")
    
    # Convert to simple format
    simple_format = chat_history.to_simple_format()
    
    # Print the converted format
    print("\nConverted to simple format:")
    for message in simple_format:
        print(f"Role: {message['role']}, Content: {message['content']}")
    
    # Convert back to Google Generative AI format
    converted_back = ChatHistory.from_simple_format(simple_format)
    
    # Print the converted back format
    print("\nConverted back to Google Generative AI format:")
    for content in converted_back.chat_history:
        print(f"Role: {content.role}, Text: {content.parts[0].text}")

if __name__ == "__main__":
    main() 