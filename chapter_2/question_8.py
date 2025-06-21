import os

from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate   
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableLambda, RunnableMap
from operator import itemgetter

load_dotenv()

def fake_db_lookup(input):

    product_name = input["question"].split()[-1].lower().rstrip("?!")

    db = {
        "notebook": "Notebook com processador Intel i7, 16GB RAM, SSD de 512GB",
        "mouse": "Mouse óptico sem fio com 1600 DPI e conexão USB",
        "fone": "Fone de ouvido com cancelamento de ruído ativo e Bluetooth 5.0"
    }

    return db.get(product_name, "Produto não encontrado")

prompt = ChatPromptTemplate.from_template("Com base na seguinte informação do produto:\n\n{product_info}\n\nResponda à pergunta: {question}")

db_tool = RunnableLambda(fake_db_lookup)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.0)

chain = RunnableMap({
    "product_info": db_tool,
    "question": itemgetter("question")
    }) | prompt | llm

result = chain.invoke({"question": "É uma boa comprar esse notebook?"})

print(result)