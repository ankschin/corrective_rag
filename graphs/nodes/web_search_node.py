from typing import Dict, Any



import sys
import os

# Get the root directory
root_dir = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), '..'),'..'))
# Add the root directory to sys.path
sys.path.insert(0, root_dir)

# Now you can import modules from the root directory
from langchain_tavily import TavilySearch
from langchain_core.documents import Document
from graphs.state import Graphstate
from dotenv import load_dotenv
load_dotenv()

web_search_tool= TavilySearch(max_results= 3)


def web_search(state: Graphstate) -> Dict[str, Any]:
    print("--Web search--")
    question= state["question"]
    documents=state['documents']


    tavily_search= web_search_tool.invoke({"query":question})
    print("----tavily results----")
    print(tavily_search)

    joined_tavily_results= "\n".join([tavily_result['content'] for tavily_result in tavily_search]) 
    web_results= Document(page_content=joined_tavily_results)

    if documents is not None:
        documents.append(web_results)
    else:
        documents= [web_results]

    return {"documents": documents, "question":question}

if __name__=="__main__":
    web_search(state={"question":"agent memory","documents": None})
    