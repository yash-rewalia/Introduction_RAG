from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
import llama_index
import os
from dotenv import load_dotenv
import sys


load_dotenv()

def main(url: str)->None:
    document = SimpleDirectoryReader(url).load_data()
    index = VectorStoreIndex.from_documents(document)
    query_engine = index.as_query_engine()
    response = query_engine.query("What is kurtosis")    
    print(response)


if __name__ == "__main__":
    main(url = r'D:\\work_yk\\RAG\\Data')