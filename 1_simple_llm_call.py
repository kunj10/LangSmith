from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from llm import chat_model
from langchain_core.output_parsers import StrOutputParser


prompt = PromptTemplate.from_template("{question}")

parser = StrOutputParser()

chain = prompt | chat_model | parser

# Run it
result = chain.invoke({"question": "What is the capital of Peru?"})
print(result)
