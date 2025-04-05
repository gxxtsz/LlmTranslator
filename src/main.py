import argparse
import yaml

from controllers.controller import Controller
from models.ollama_interaction import OllamaLLMInteraction
from readers.txt_reader import TxtReader
from writers.txt_writer import TxtWriter
from logger import logger

def main():
    parser = argparse.ArgumentParser(description='Run translation with configuration file.')
    parser.add_argument('--config', type=str, default='config/default.yml', help='Path to the configuration file.')
    args = parser.parse_args()

    try:
        # 读取配置文件
        with open(args.config, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)

        reader = TxtReader(config['reader'])
        writer = TxtWriter(config['write'])
        llm_interactor = OllamaLLMInteraction(config['model'])

        controller = Controller(config['controller'], reader, writer, llm_interactor)
        controller.run_translation()

    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    main()