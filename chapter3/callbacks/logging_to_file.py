from langchain.callbacks import FileCallbackHandler
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from loguru import logger

logfile = "output.log"
logger.add(logfile, colorize=True, enqueue=True)
handler = FileCallbackHandler(logfile)

llm = ChatOllama(model="qwen2.5:0.5b")
prompt = PromptTemplate.from_template("1 + {number} = ")

# 这个链将同时向标准输出打印（因为 verbose=True）并写入 'output.log'
# 如果 verbose=False，FileCallbackHandler 仍会写入 'output.log'
chain = LLMChain(llm=llm, prompt=prompt, callbacks=[handler], verbose=False)
answer = chain.invoke({"number": 1})
logger.info(answer)