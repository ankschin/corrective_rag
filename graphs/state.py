from typing import List, TypedDict


class Graphstate:
    """
    Class to represent the state of a graph.
    
    Attributes:
        question (str): The question being asked about the graph.
        generation (int): The LLM generation.
        web_search (bool): Whether to add search.
        documents (List[Document]): List of documents.

    """


    question: str
    generation: int
    web_search: bool
    documents: List[str]

if __name__=="__main__":
    pass