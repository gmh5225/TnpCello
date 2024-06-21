import os
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
import qdrant_client
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_vector_store():
    client = qdrant_client.QdrantClient(
        os.getenv("HOST"),
        api_key=os.getenv("API_KEY")
    )
    embeddings = OpenAIEmbeddings()

    vector_store = Qdrant(
        client=client,
        collection_name=os.getenv("COLLECTION_NAME"),
        embeddings=embeddings,
    )
    return vector_store

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(model="text-davinci-003"),
    chain_type="stuff",
    retriever=get_vector_store().as_retriever()
)

query = "please give all job listings available"

response = qa.run(query)

print(response)
