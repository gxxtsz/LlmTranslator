import re
import os

from logger import logger
from readers.base_reader import BaseReader

class TxtReader(BaseReader):
    def __init__(self, config):
        super().__init__(config)
        self.min_length = config.get('min_length', 100)
        self.max_length = config.get('max_length', 500)

    def read(self) -> list[str]:
        """
        读取文本文件并将其内容分割成合适的段落。

        读取文件内容，按行分割，根据最小和最大长度要求合并和分割段落。

        Returns:
            list: 包含分割后段落的列表。
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            lines = [line.strip() + "\n" for line in content.split('\n') if line.strip()]
            result = []
            current = ""
            for s in lines:
                # 如果当前段落和新行的总长度小于最小长度，则合并
                if len(current) + len(s) < self.min_length:
                    current = current + s if current else s
                else:
                    if current:
                        # 对当前段落进行分割并添加到结果列表
                        result.extend(self._split_string(current))
                        current = ""
                    if len(s) < self.min_length:
                        current = s
                    else:
                        # 对新行进行分割并添加到结果列表
                        result.extend(self._split_string(s))

            if current:
                result.extend(self._split_string(current))
            return result
        
        except FileNotFoundError:
            logger.error(f"错误: 文件 {self.file_path} 未找到。")
        except Exception as e:
            logger.error(f"错误: 发生了未知错误: {e}")

    def _split_string(self, s):
        return [s[i:i + self.max_length] for i in range(0, len(s), self.max_length)]



