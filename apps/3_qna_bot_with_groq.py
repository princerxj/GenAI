from dotenv import load_dotenv
load_dotenv() 

from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langgraph.checkpoint.memory import MemorySaver
from langchain.agents import create_agent

import streamlit as st 

llm = ChatGroq(model = "openai/gpt-oss-120b", streaming=True)
search = GoogleSerperAPIWrapper()
tools = [search.run]

if "memory" not in st.session_state : 
    st.session_state.memory = MemorySaver()

if "history" not in st.session_state : 
    st.session_state.history = []

agent = create_agent(
    model = llm, 
    tools = tools, 
    checkpointer=st.session_state.memory, 
    system_prompt="You are an agent with access to a Google search tool. "
    "You do NOT have real-time or up-to-date information on your own. "
    "For ANY question involving current events, prices, dates, scores, "
    "or anything that could have changed recently, you MUST call the "
    "search tool before answering. Never say you cannot access real-time data — "
    "use the search tool instead.", 
)


### Building Web Interface 
st.subheader("Quickanswer - Get answers at the speed of your thoughts")

query = st.chat_input("ask anything ?")

for message in st.session_state.history : 
    role = message["role"]
    content = message["content"]

    st.chat_message(role).markdown(content)


if query : 
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role" : "user", "content" : query})

    response = agent.stream(
        {"messages" : [{"role": "user", "content" : query}]}, 
        {"configurable" : {"thread_id" : "1"}}, 
        stream_mode="messages"
    )

    ai_container = st.chat_message("ai")
    with ai_container : 
        space = st.empty()

        message = ""

        for chunk in response : 
            message = message + chunk[0].content
            space.write(message)

        st.session_state.history.append({"role" : "AI", "content" : message})