from langchain_community.llms import Ollama
import langchain
from langchain.globals import set_debug

llm = Ollama(model="qwen2.5:0.5b")
langchain.debug = True
result = llm.invoke("你是谁？")
print(result)