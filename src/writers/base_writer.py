class BaseWriter:
    def __init__(self, config):
        self.file_path = config.get('file_path', 'output.txt')

    def write(self, translated_text):
        """
        写入翻译后文本的方法，需在子类中实现具体逻辑
        :param translated_text: 翻译后的文本
        """
        raise NotImplementedError("The 'write' method must be implemented in subclasses.")
    