import os

from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

story_prompt = ChatPromptTemplate.from_template("Write a story about {topic}")

story_chain = story_prompt | llm | StrOutputParser()

analysis_prompt = ChatPromptTemplate.from_template("Analyze the following story's mood:\n {story}")

analysis_chain = analysis_prompt | llm | StrOutputParser()

story_with_analysis = story_chain | analysis_chain

story_analysis = story_with_analysis.invoke({"topic": "a cat and a dog"})

print("\nAnalysis:", story_analysis)