from typing import TypedDict, List
from langchain_core.messages import HumanMessage #for human message

#from langchain_openai import ChatOpenAI #for openai model
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv #for loading environment variables

load_dotenv()  #loading environment variables

class AgentState(TypedDict):
    messages: List[HumanMessage]

#llm = ChatOpenAI(model="gpt-4o-mini")
llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash")
def process(state: AgentState)-> AgentState:
    """Process the state of the agent"""
    response = llm.invoke(state["messages"])
    print(f"\nAI response: {response.content}")
    return state



graph = StateGraph(AgentState)

graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()

user_input = input("Enter your message: ")
while user_input != "exit":
    agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("Enter your message: ")

