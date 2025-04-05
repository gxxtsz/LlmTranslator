from logger import logger
from writers.base_writer import BaseWriter

class TxtWriter(BaseWriter):
    def __init__(self, config):
        super().__init__(config)
        try:
            self.file = open(self.file_path, 'w', encoding='utf-8')
        except Exception as e:
            logger.error(f"打开文件{self.file_path}时出现错误: {e}")

    def write(self, translated_text):
        try:
            self.file.write(translated_text)
            self.file.flush()
        except Exception as e:
            logger.error(f"写入文件{self.file_path}时出现错误: {e}")

    def close(self):
        try:
            self.file.close()
        except Exception as e:
            logger.error(f"关闭文件{self.file_path}时出现错误: {e}")