from langchain_community.llms import Ollama
from langchain.globals import set_llm_cache
from langchain.cache import InMemoryCache

set_llm_cache(InMemoryCache())

#配置模型信息
llm = Ollama(model="qwen2.5:0.5b")

#调用大语言模型的预测功能
print(llm.invoke("中国的首都是哪个城市？"))