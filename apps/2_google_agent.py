from dotenv import load_dotenv
load_dotenv() 

from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

model = ChatGroq(model = "openai/gpt-oss-120b")
search = GoogleSerperAPIWrapper()

agent = create_agent(
    model = model, 
    tools = [search.run], 
    system_prompt="You are an agent with access to a Google search tool. "
    "You do NOT have real-time or up-to-date information on your own. "
    "For ANY question involving current events, prices, dates, scores, "
    "or anything that could have changed recently, you MUST call the "
    "search tool before answering. Never say you cannot access real-time data — "
    "use the search tool instead.", 
    checkpointer=MemorySaver()
)

while True : 
    query = input("User : ")
    if query.lower() in ["quit", "exit", "bye"] : 
        print("GoodBye !!!!")
        break 

    response = agent.invoke({"messages" : [{"role" : "user", "content" : query}]}, {"configurable" : {"thread_id" : "prince"}})
    print("AI : " , response["messages"][-1].content)