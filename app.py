import streamlit as st

from langchain_community.vectorstores import Chroma

def search():
    from langchain_huggingface import HuggingFaceEmbeddings
    embeddings = HuggingFaceEmbeddings()

    return Chroma(persist_directory="chroma",embedding_function=embeddings).as_retriever(search_kwargs={"k":5})

st.title("Muhammad Faizan Mumtaz Blog Site")

if prompt:=st.chat_input("Search for articles..."):
    st.markdown(f"## {prompt}")
    with st.spinner("Searching..."):
        for results in search().invoke(prompt):
            with st.expander(results.metadata['title']):
                st.write(results.page_content)