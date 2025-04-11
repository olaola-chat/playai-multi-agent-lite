from core.config.gemini_model_config import ModelName
from core.api.gemini_api import generate_text_with_stream, generate_text
from core.prompt.gemini_prompt import GeminiPrompt, ChatHistory
from core.config.gemini_model_config import GeminiModelConfig
from google.genai.types import Content,Part
from core.orchestra import AgentOrchestra

def init_chat_history():
    return ChatHistory(
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

    
if __name__ == "__main__":

    agent_orchestra = AgentOrchestra()
    chat_history = init_chat_history()
    model_configs = {
        "router_agent": GeminiModelConfig(
            model=ModelName.GEMINI_2_0_FLASH,
            temperature=0.5,
            top_p=1,
            max_tokens=256
        ),
        "agent_1": GeminiModelConfig(
            model=ModelName.GEMINI_2_0_FLASH_LITE,
            temperature=1,
            top_p=0.5,
            max_tokens=512
        ),
        "agent_2": GeminiModelConfig(
            model=ModelName.GEMINI_2_0_FLASH_LITE,
            temperature=1,
            top_p=0.7,
            max_tokens=512
        ),
        "agent_3": GeminiModelConfig(
            model=ModelName.GEMINI_2_0_FLASH_LITE,
            temperature=1,
            top_p=0.6,
            max_tokens=512
        ),
        "agent_4": GeminiModelConfig(
            model=ModelName.GEMINI_2_0_FLASH_LITE,
            temperature=1,
            top_p=0.5,
            max_tokens=512
        )
    }

    test_cases_prompt = [
        "你好丑啊",
        "你真漂亮",
        "我心情不好",
        "你是傻傻的",
        "你喜欢吃什么",
        "我好累啊",
        "你真别扭",
        "不想上班",
        "你工资多少",
        "你真搞笑",
        "你真无聊",
        "说个笑话我听"
    ]

    for prompt in test_cases_prompt:

        print("--------------------------------")
        print("用户问:", prompt)
        print(agent_orchestra.multi_agent_response(chat_history, prompt, model_configs))

    print("--------------------------------")

