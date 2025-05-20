from dotenv import load_dotenv


from langgraph.graph import END, StateGraph
from graphs.consts import RETRIEVE, GENERATE, GRADE_DOCUMENTS, WEBSEARCH
from graphs.nodes import generation_chain, grade_documents,retrieve, web_search
from graphs.state import Graphstate

load_dotenv()

def decide_to_generate(state):
    print("--Assess graded docs--")

    if state["web_search"]:
        print("")
        return WEBSEARCH
    
    else:
        print("")
        return GENERATE
    

workflow= StateGraph(Graphstate)

workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(GENERATE, generation_chain)
workflow.add_node(WEBSEARCH, web_search)


workflow.set_entry_point(RETRIEVE)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)
workflow.add_conditional_edges(GRADE_DOCUMENTS, decide_to_generate, {WEBSEARCH:WEBSEARCH, GENERATE:GENERATE})
workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)


app= workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph.png")
