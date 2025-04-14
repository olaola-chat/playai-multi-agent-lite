from core.config.gemini_model_config import GeminiModelConfig, ModelName


predefine_model_configs = {
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