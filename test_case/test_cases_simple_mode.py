from core.config.gemini_model_config import ModelName
from core.prompt.gemini_prompt import ChatHistory
from core.config.gemini_model_config import GeminiModelConfig
from core.config.model_predefine_config import predefine_model_configs
from google.genai.types import Content,Part
from core.orchestra import AgentOrchestra

def init_chat_history():
    return ChatHistory(
        chat_history=[
            Content(
                role="user",
                parts=[
                    Part.from_text(text="我想摆烂")
                ]
            ),
            Content(
                role="model",
                parts=[
                    Part.from_text(text="那还等啥？一起快乐摆烂，做一条无忧无虑的咸鱼呀！（≥V≤）/")
                ]
            ),

        ]
    )

    
if __name__ == "__main__":

    agent_orchestra = AgentOrchestra()
    chat_history = init_chat_history()
   

    test_cases_prompt = [
        # "你好丑啊",
        # "你真漂亮",
        # "我心情不好",
        # "你是傻傻的",
        # "你喜欢吃什么",
        # "我好累啊",
        # "你真别扭",
        # "不想上班",
        # "你工资多少",
        # "你真搞笑",
        # "你真无聊",
        # "说个笑话我听"
        "怎么个躺法"
    ]

    for prompt in test_cases_prompt:

        print("--------------------------------")
        print("用户问:", prompt)
        print(agent_orchestra.multi_agent_response(chat_history.to_simple_format(), prompt, predefine_model_configs))

    print("--------------------------------")

