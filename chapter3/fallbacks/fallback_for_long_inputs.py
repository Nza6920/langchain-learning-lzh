from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI

# 需要 export OPENAI_API_KEY='yourkey'

# 处理短输入
short_llm = ChatOpenAI()
# 处理长输入
long_llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

# 设置短输入模型回退
llm = short_llm.with_fallbacks([long_llm])

# 先尝试使用不支持长输入的模型
inputs = "下一个数字是: " + ", ".join(["1", "2"] * 3000)
try:
    print(short_llm.invoke(inputs))
except Exception as e:
    print(e)

try:
    print(llm.invoke(inputs))
except Exception as e:
    print(e)
