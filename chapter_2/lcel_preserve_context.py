import os

from dotenv import load_dotenv

from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

story_prompt = ChatPromptTemplate.from_template("Write a story about {topic}")

story_chain = story_prompt | llm | StrOutputParser()

analysis_prompt = ChatPromptTemplate.from_template("Analyze the following story's mood:\n {story}")

analysis_chain = analysis_prompt | llm | StrOutputParser()

story_with_analysis = story_chain | analysis_chain

enhanced_chain = RunnablePassthrough.assign(story=story_chain).assign(analysis=analysis_chain)

result = enhanced_chain.invoke({"topic": "a cat and a dog"})

print("\nAnalysis:", result.keys())
print("\nAnalysis:", result["story"])
print("\nAnalysis:", result["analysis"])