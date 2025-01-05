from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import HumanMessage
from langchain.callbacks.base import AsyncCallbackHandler, BaseCallbackHandler
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.outputs import LLMResult

class MyCustomHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        print(f"自定义回调处理器, token: {token}")

chat = ChatOllama(model="qwen2.5:0.5b", callbacks=[MyCustomHandler()])

chat.invoke([HumanMessage(content="青海的省会是？")])
