import requests

from logger import logger
from models.base_llm_interaction import BaseLLMInteraction

class OllamaLLMInteraction(BaseLLMInteraction):
    def __init__(self, config):
        super().__init__()
        self.model_name = config.get('model_name', 'qwen2.5:latest')
        self.base_url = config.get('base_url', 'http://localhost:11434')

    def translate(self, text: str) -> str:
        url = f"{self.base_url}/api/generate"
        data = {
            "model": self.model_name,
            "prompt": text,
            "stream": False
        }
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            result = response.json()
            translated_text = result.get('response', '')
            return translated_text
        except requests.RequestException as e:
            logger.error(f"请求出错: {e}")
            return None
        except ValueError as e:
            logger.error(f"解析响应出错: {e}")
            return None
        

if __name__ == '__main__':
    interaction = OllamaLLMInteraction({})
    prompt = "将以下文本翻译成中文: hello world"
    result = interaction.translate(prompt)
    print(result)
