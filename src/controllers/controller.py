from tqdm import tqdm
from logger import logger

class TqdmToLogger:
    def __init__(self, logger):
        self.logger = logger

    def write(self, buf):
        if buf.strip():
            self.logger.info(buf.rstrip())

    def flush(self):
        pass


class Controller:
    def __init__(self, config, reader, writer, llm_interactor):
        """
        初始化控制模块
        :param reader: 文档读取器实例，继承自 BaseDocumentReader
        :param writer: 文档写入器实例，继承自 BaseDocumentWriter
        :param llm_interactor: 大模型交互器实例，继承自 BaseLLMInteraction
        """
        self.reader = reader
        self.writer = writer
        self.llm_interactor = llm_interactor

        self.source_language = config['source_language']
        self.target_language = config['target_language']

        self.tqdm_logger = TqdmToLogger(logger)

    def run_translation(self):
        """
        执行翻译流程的接口，包含读取文档、调用大模型翻译、写入结果等步骤
        """
        try:
            text_list = self.reader.read()
            for text in tqdm(text_list, file=self.tqdm_logger, desc="Translation progress"):
                try:
                    translated_text = self.llm_interactor.translate(self._generate_prompt(text))
                    # print(translated_text)
                    self.writer.write(translated_text)
                except Exception as e:
                    # 记录翻译过程中的异常
                    logger.error(f"翻译文本时出错: {text[:50]}... 错误信息: {e}")
            self.writer.close()
        except Exception as e:
            # 记录读取文档时的异常
            logger.error(f"读取文档时出错: {e}")

    def _generate_prompt(self, text):
        prompt = f"将以下文本从{self.source_language}翻译成{self.target_language}:\n{text}"
        return prompt


    