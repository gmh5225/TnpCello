from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
import qdrant_client
from dotenv import load_dotenv
from splitter import texts
import os

load_dotenv()

# Initialize Qdrant client
client = qdrant_client.QdrantClient(
    os.getenv("HOST"),
    api_key=os.getenv("API_KEY")
)

# Configure vector parameters
vector_config = qdrant_client.http.models.VectorParams(
    size=1536,
    distance=qdrant_client.http.models.Distance.COSINE
)

# Check if collection exists, if not create it
try:
    client.get_collection(collection_name=os.getenv("COLLECTION_NAME"))
except Exception as e:
    print(type(e))  # Print the type of the exception
    client.create_collection(
        collection_name=os.getenv("COLLECTION_NAME"),
        vectors_config=vector_config,
    )

# Get OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_KEY')

# Initialize OpenAI embeddings
embeddings = OpenAIEmbeddings()

# Initialize Qdrant vector store
vector_store = Qdrant(
    client=client,
    collection_name=os.getenv("COLLECTION_NAME"),
    embeddings=embeddings,
)

# Add texts to the vector store
vector_store.add_texts(texts)
