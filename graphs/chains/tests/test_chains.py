from ingestion import retriever
from graphs.chains.generation import generation_chain
from pprint import pprint


def test_foo() -> None:
    assert 1==1




def test_generation_chain() -> None:
    question= "agent memory"
    docs= retriever.invoke(question)
    generation= generation_chain.invoke({"context":docs, "question": question})
    pprint(generation)