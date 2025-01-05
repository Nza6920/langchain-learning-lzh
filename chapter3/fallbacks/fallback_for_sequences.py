from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama

prompt_template = """说明：您应该在回复中始终包含赞美之词。
问题: 为什么你喜欢{city}?"""
prompt = PromptTemplate.from_template(prompt_template)

# 使用一个错误的模型名称来轻松创建一个会报错的链式调用
bad_llm = ChatOllama(model="gpt-fake:0.5b")
bad_chain = prompt | bad_llm

# 构建一个正确的链
good_llm = ChatOllama(model="qwen2.5:0.5b")
good_chain = prompt | good_llm

# 将两条链结合到一起
chain = bad_chain.with_fallbacks([good_chain])
print(chain.invoke({"city": "西宁"}))
