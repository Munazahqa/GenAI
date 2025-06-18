"""use diff msg types , human msg ,AI msg
maintains a history of messages between human and AI

"""


from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, AIMessage #for human message

#from langchain_openai import ChatOpenAI #for openai model
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv #for loading environment variables

load_dotenv()  #loading environment variables

class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]

   

#llm = ChatOpenAI(model="gpt-4o-mini")
llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash")
def process(state: AgentState)-> AgentState:
    response = llm.invoke(state["messages"])
    state["messages"].append(AIMessage(content=response.content))
    
    print(f"\nAI response: {response.content}")
    
    #print("current state: ", state['messages'])
    return state



graph = StateGraph(AgentState)

graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()


conversation_history = []  #to maintain the history of messages

user_input = input("Enter your message: ")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result=agent.invoke({"messages": conversation_history})
    conversation_history = result["messages"]
    user_input = input("Enter your message: ")



with open("login.txt", "w") as f:
    f.write("Your conversation history is: \n")

    for message in conversation_history:
        if isinstance(message, HumanMessage):
            f.write(f"Human: {message.content}\n")
        elif isinstance(message, AIMessage):
            f.write(f"AI: {message.content}\n")
    f.write("\nEnd of conversation")

    print("conversation history saved to login.txt")







