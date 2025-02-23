from langchain_community.llms.ollama import Ollama
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field


# output_parser = DatetimeOutputParser()
# print(output_parser.get_format_instructions())

class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")


llm = Ollama(model="qwen2.5:0.5b")

parser = PydanticOutputParser(pydantic_object=Joke)
# print(parser.get_format_instructions())

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

joke_query = "Tell me a joke."
_input = prompt.format_prompt(query = joke_query)
print(_input)
output = llm.invoke(_input.to_string())
print(parser.parse(output))
