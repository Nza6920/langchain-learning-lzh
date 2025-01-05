import asyncio
from typing import Any, Dict, List

from langchain.callbacks.base import AsyncCallbackHandler, BaseCallbackHandler
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.outputs import LLMResult


class MyCustomSyncHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        print(f"Sync handler being called in a `thread_pool_executor`: token: {token}")

class MyCustomAsyncHandler(AsyncCallbackHandler):
    """Async callback handler that can be used to handle callbacks from langchain."""
    async def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Run when chain starts running."""
        print("zzzz....")
        await asyncio.sleep(0.3)
        class_name = serialized["name"]
        print("LLM正在启动")

    async def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Run when chain ends running."""
        print("zzzz....")
        await asyncio.sleep(0.3)
        print("LLM结束")

qwen_llm = ChatOllama(model="qwen2.5:0.5b", callbacks=[MyCustomSyncHandler(), MyCustomAsyncHandler()])

asyncio.run(qwen_llm.agenerate(messages = [[HumanMessage(content="告诉我西宁的特产")]]))


