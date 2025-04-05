class BaseLLMInteraction:
    def __init__(self):
        """
        初始化方法，可在子类中进行扩展
        """
        pass

    def translate(self, text):
        """
        翻译方法，需要在子类中实现具体逻辑
        :param text: 待翻译的文本
        :return: 翻译后的文本
        """
        raise NotImplementedError("The 'translate' method must be implemented in subclasses.")

    