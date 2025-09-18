from llm import chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
os.environ["LANGCHAIN_PROJECT"]  = "Sequential LLM App"
prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)
parser = StrOutputParser()

model = chat_model

chain = prompt1 | model | parser | prompt2 | model | parser

config = {
    'tags ' : ['llm app', 'report' , 'summarization'],
    'metadata' : {'model' : 'Google Gemini'}
}

result = chain.invoke({'topic': 'Unemployment in India'})

print(result)
