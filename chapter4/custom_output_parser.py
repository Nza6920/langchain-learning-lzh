# 从 typing 模块导入 Iterable 类型，用于表示可迭代对象
from typing import Iterable

# 从 langchain_community.llms 模块导入 Ollama 类
from langchain_community.llms import Ollama
# 从 langchain_core.messages 模块导入 AIMessage 和 AIMessageChunk 类，用于处理 AI 消息
from langchain_core.messages import AIMessage, AIMessageChunk
from langchain_core.runnables import RunnableGenerator

# 创建一个 Ollama 对象，使用 "qwen2.5:0.5b" 模型
llm = Ollama(model="qwen2.5:0.5b")


def parse(ai_message: AIMessage) -> str:
    """
    解析 AI 消息。
    参数:
    ai_message (AIMessage): 要解析的 AI 消息对象
    返回:
    str: 解析后的字符串，这里简单地将消息中的字母大小写进行互换
    """
    # 使用swapcase() 方法来互换字母大小写，并返回结果
    return ai_message.swapcase()


# chain = llm | parse
# # 调用链的 invoke 方法，并传入字符串 "hello" 作为输入
# output = chain.invoke("hello")
# print(output)

def streaming_parse(chunks: Iterable[AIMessageChunk]) -> Iterable[str]:
    for chunk in chunks:
        yield chunk.swapcase()

streaming = RunnableGenerator(streaming_parse)
chain = llm | streaming
for chunk in chain.stream('hello'):
    print(chunk, end="|", flush=True)
