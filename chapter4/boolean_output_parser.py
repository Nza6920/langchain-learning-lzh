from langchain_core.exceptions import OutputParserException  # 导入OutputParserException异常类
from langchain_core.output_parsers import BaseOutputParser  # 导入BaseOutputParser基类
# 从 langchain_community.llms 模块导入 Ollama 类
from langchain_community.llms import Ollama
# 创建一个 Ollama 对象，使用 "qwen:1.8b" 模型
llm = Ollama(model="qwen2.5:0.5b")

class BooleanOutputParser(BaseOutputParser[bool]):
    """Custom boolean parser."""  # 类的文档字符串

    # 定义了两个类属性，表示布尔值"真"和"假"的字符串表示
    true_val: str = "YES"
    false_val: str = "NO"

    # parse方法，用于将传入的字符串解析为布尔值
    def parse(self, text: str) -> bool:
        # 清理文本，去除首尾空格并转换为大写
        cleaned_text = text.strip().upper()
        # 检查清理后的文本是否匹配"真"或"假"的值
        if (self.true_val.upper() not in cleaned_text.upper()) & (self.false_val.upper() not in cleaned_text.upper()):
            # 如果不匹配，则抛出异常
            raise OutputParserException(
                f"BooleanOutputParser expected output value to either be "
                f"{self.true_val} or {self.false_val} (case-insensitive). "
                f"Received {cleaned_text}."
            )
            # 返回解析结果，如果cleaned_text等于"YES"，则返回True，否则返回False
        return cleaned_text == self.true_val.upper()

        # _type属性，返回解析器的类型字符串

    @property
    def _type(self) -> str:
        return "boolean_output_parser"

# 创建BooleanOutputParser类的实例
parser = BooleanOutputParser()
chain = llm | parser
print(chain.invoke("请回复 yes 单词, 不要有其他单词."))

