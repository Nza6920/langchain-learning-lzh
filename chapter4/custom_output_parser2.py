from typing import List
from langchain_core.exceptions import OutputParserException
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import BaseGenerationOutputParser
from langchain_core.outputs import ChatGeneration, Generation
from langchain_community.chat_models import ChatOllama

class StrInvertCase(BaseGenerationOutputParser[str]):
    """反转消息中字符大小写的示例解析器。"""
    def parse_result(self, result: List[Generation], *, partial: bool = False) -> str:
        """将模型生成列表解析为特定格式。
       参数：
       result：要解析的Generations的列表。假设Generations为单个模型输入的不同候选输出。
       许多解析器假设只传递了一个生成。我们将为此断言
       部分：是否允许部分结果。这用于解析器支持流媒体。
        """
        if len(result) != 1:
            raise NotImplementedError(
                "此输出解析器只能与单个生成一起使用。"
            )
        generation = result[0]
        if not isinstance(generation, ChatGeneration):
            # Say that this one only works with chat generations
            raise OutputParserException(
                "该输出解析器只能与聊天生成一起使用。"
            )
        return generation.message.content.swapcase()

# 创建一个 Ollama 对象，使用 "qwen2.5:0.5b" 模型
chat = ChatOllama(model="qwen2.5:0.5b")
chain = chat | StrInvertCase()
print(chain.invoke("Hello"))