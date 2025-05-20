from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader

import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain_community.docstore.in_memory import InMemoryDocstore
import faiss

load_dotenv()

# urls=["https://medium.com/@j13mehul/rag-part-7-evaluation-fb8134792e09",
#         "https://dkaarthick.medium.com/ragas-for-rag-in-llms-a-comprehensive-guide-to-evaluation-metrics-3aca142d6e38",
#         "https://myscale.com/blog/naive-rag-vs-advanced-rag/",]


# docs= [WebBaseLoader(url).load() for url in urls]
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# docs_list= [item for sublist in docs  for item in sublist]

# text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=0)


# doc_splits= text_splitter.split_documents(docs_list)

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")


index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))

# vectorstore = FAISS.from_documents(documents= doc_splits,
#                                     embedding=embeddings,
#                                     docstore=InMemoryDocstore(), index_to_docstore_id={},
#                                 )

# vectorstore.save_local("faiss_index")




retriever = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# res= new_db.similarity_search("types of rag") 

# print(res)
