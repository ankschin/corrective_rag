from typing import Dict, Any

from graphs.state import Graphstate
from graphs.chains.retrieval_grader import retriever_grader


def grade_documents(state: Graphstate) -> Dict[str, Any]:
    print("check docs relevance to question")
    question= state["question"]
    documents= state["documents"]

    filtered_docs = []

    web_search = False ## if found any docs not relevant to question toggle web searh to True

    for doc in documents:
        score= retriever_grader.invoke({"question": question, "documnet": doc.page_content})
        grade= score.binary_score

        if grade.str.lower() == "yes":
            print("--Doc relevant--")
            filtered_docs.append(doc)
        else:
            print("--Doc not relevant--")
            web_search = True
            continue