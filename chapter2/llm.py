from langchain_community.llms import Ollama

llm = Ollama(model="qwen2.5:0.5b")

print(llm.invoke("你是谁？"))