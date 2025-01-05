from langchain_community.chat_models import ChatOllama
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

chat = ChatOllama(model="qwen2.5:0.5b")

template = "你是一个翻译助理，请将用户输入的内容由{input_language}直接翻译为{out_language}"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

prompt = chat_prompt.format_prompt(input_language="中文",
                                   out_language="英语",
                                   text="我是一个非常非常帅的人。").to_messages()
result = chat.invoke(prompt)
print(result.content)
