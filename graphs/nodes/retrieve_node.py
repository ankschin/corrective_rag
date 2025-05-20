from typing import Dict, Any

from graphs.state import Graphstate
from ingestion import retriever


def retrieve(state: Graphstate) -> Dict[str, Any]:
    print("--Retrrieve--")
    question= state['question']

    documents= retriever.invoke(question)

    return {"documents":documents, "question": question}