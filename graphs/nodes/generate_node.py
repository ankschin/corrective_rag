from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain import hub

from langchain_openai import ChatOpenAI

llm= ChatOpenAI(temperature=0)

prompt= """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
            Question: {question} 
            Context: {context} 
            Answer:"""

start_prompt = PromptTemplate.from_template(prompt)
generation_chain= start_prompt | llm | StrOutputParser()

