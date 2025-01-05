from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI
from unittest.mock import patch
import httpx
from openai import RateLimitError
from langchain_core.prompts import ChatPromptTemplate

request = httpx.Request("GET", "/")
response = httpx.Response(200, request=request)
error = RateLimitError("rate limit", response=response, body="")

# 将 max_retries 设置为 0，以避免对 RateLimits 等进行重试
openai_llm = ChatOpenAI(max_retries=0, api_key='fake')
qwen_llm = ChatOllama(model="qwen2.5:0.5b")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个贴心的助手，总会在回复中附上赞美之词。",
        ),
        ("human", "为什么你喜欢{city}"),
    ]
)
# 尝试使用 qwen_llm 作为备选方案
llm = openai_llm.with_fallbacks([qwen_llm])

chain = prompt | llm

with patch("openai.resources.chat.completions.Completions.create", side_effect=error):
    try:
        print(chain.invoke({"city": "西宁"}))
    except RateLimitError:
        print("遇到错误")
