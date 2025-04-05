class BaseReader:
    def __init__(self, config):
        self.file_path = config.get('file_path')

    def read(self):
        """
        读取文件内容的方法，需要在子类中实现具体逻辑
        :return: 文件中的文本内容
        """
        raise NotImplementedError("The 'read' method must be implemented in subclasses.")
    