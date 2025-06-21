import os

from dotenv import load_dotenv

from langchain_openai import OpenAI
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.llms import FakeListLLM
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

#openai_llm = OpenAI()

#gemini_pro_llm = GoogleGenerativeAI(model="gemini-1.5-pro")

#response = openai_llm.invoke("What is the capital of France?")
#response = gemini_pro_llm.invoke("What is the capital of France?")

#print(response)

#fake_llm = FakeListLLM(responses=["Hello, world!"])

#result = fake_llm.invoke("What is the capital of France?")

#print(result)

#chat_gemini_pro_llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

#messages = [
#    SystemMessage(content="You are a helpful assistant that can answer questions."),
#    HumanMessage(content="What is the capital of France?"),
#]

#response = chat_gemini_pro_llm.invoke(messages)

#print(response)

question_template = ChatPromptTemplate.from_template("What is the capital of {country}?")

question_with_context_template = ChatPromptTemplate.from_template("""
    You are a helpful assistant that can answer questions.
    You are given a question and a context.
    You need to answer the question based on the context.
    Question: {question}
    Context: {context}
""")

prompt_text = question_template.format(country="France")


