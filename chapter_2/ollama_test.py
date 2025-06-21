import os

from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate   
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOllama(model="deepseek-r1:1.5b", temperature=0.0)

prompt = ChatPromptTemplate.from_template("Explain the concept of {concept} in a way that is easy to understand.")

chain = prompt | llm | StrOutputParser()

result = chain.invoke({"concept": "AI"})

print(result)

