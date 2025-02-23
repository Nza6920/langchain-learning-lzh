from typing import Any, Dict, List, Union

from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks.base import BaseCallbackHandler
from langchain_community.llms import Ollama
from langchain_core.agents import AgentAction


# 首先，定义自定义回调处理器实现
class MyCustomHandlerOne(BaseCallbackHandler):
    def on_llm_start(
            self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        print(f"on_llm_start {serialized['name']}")

    def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
        print(f"on_new_token {token}")

    def on_llm_error(
            self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """Run when LLM errors."""

    def on_chain_start(
            self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        print(f"on_chain_start {serialized['name']}")

    def on_tool_start(
            self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
    ) -> Any:
        print(f"on_tool_start {serialized['name']}")

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        print(f"on_agent_action {action}")


class MyCustomHandlerTwo(BaseCallbackHandler):
    def on_llm_start(
            self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        print(f"on_llm_start (I'm the second handler!!) {serialized['name']}")


# 实例化处理器
handler1 = MyCustomHandlerOne()
handler2 = MyCustomHandlerTwo()
llm = Ollama(model="qwen2.5:0.5b", callbacks=[handler2])


#  设置代理。只有“llm”会为handler2发出回调
tools = load_tools(["llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# handler1 的回调将由参与 Agent 执行的每个对象（llm、llmchain、tool、agent executor）发出
agent.run("影子为什么有吸力?", callbacks=[handler1])
