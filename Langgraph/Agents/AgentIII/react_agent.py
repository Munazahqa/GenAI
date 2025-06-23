"""Objectives:
1. How to creat tools in LangGraph
2. How to Creat reach Graph
3. work with diff types of Messages such as ToolMessages
4. Test out robustness of our graph.

Main Goal: Creat a robust React Agent """



from typing import Annotated, Sequence, TypedDict
#Annotated - provides additional context without affecting the type itself means if creating type dict where there is email key(str), email should have some formate like abcgmail.com, but if we pass any other formate like abcd-gmail.com, it will pass as its also str, but annotaed solve this problem. example: 
"""email = Annotated[str, "Email should be in the form of abc@gmail.com"]
print(email.__metadata__)"""






#Sequence - to automatically handle the state updates for sequencs such as by adding new messages to a chat history, handle graph manipulation.

#TypedDict - a dictionary with typed keys and values





from dotenv import load_dotenv  
from langchain_core.messages import BaseMessage # The foundational class for all message types in LangGraph
from langchain_core.messages import ToolMessage # Passes data back to LLM after it calls a tool such as the content and the tool_call_id
from langchain_core.messages import SystemMessage # Message for providing instructions to the LLM
#from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.graph.message import add_messages  #reducer function: just a rule that controls how updates from nodes are combined with the existing state, tells how to merge new data into the current state, without reducer, uodate would have replaced the existing value entirely.as
"""
#without reducer
state = {"messages": ["hi1"]}
update = {"messages": ["hi2"]}  #hi2 overwrite hi1
new_state = {"messages": ["hi3"]}

#with reducer
state = {"messages": ["hi1"]}
update = {"messages": ["hi2"]}   #with reducer it will append hi2 to hi1.
new_state = {"messages": ["hi3"]}

#add_messages is a reducer ftn that allow as to append the state into the existing state, without any overwrite.
"""




from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode


load_dotenv()



class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]  #annotated[datatype, metadata]


@tool
def add(a: int, b: int):
    """this is an addition ftn"""  #docstring is imp if discription is not provided, it will not work.

    return a + b


tools = [add]
#model = ChatOpenAI(model="gpt-4o"). bind_tools(tools)
model = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash"). bind_tools(tools)


def model_call(state: AgentState)-> AgentState:
    """call the model and return the response"""

    system_prompt = SystemMessage(content="You are a helpful assistant, please answer my questions")
    response = model.invoke([system_prompt] + state["messages"])
    return {"messages": [response]}

#looping logic
def should_continue(state: AgentState): 
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls: 
        return "end"
    else:
        return "continue"
    
#defininh the graph
graph = StateGraph(AgentState)
graph.add_node("our_agent", model_call)


tool_node = ToolNode(tools=tools)
graph.add_node("tools", tool_node)

graph.set_entry_point("our_agent")

graph.add_conditional_edges(
    "our_agent",
    should_continue,
    {
        "continue": "tools",
        "end": END,
    },
)

graph.add_edge("tools", "our_agent")

app = graph.compile()

def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

inputs = {"messages": [("user", "Add 34 + 21 and then multiply the result by 6. Also tell me a joke please.")]}
print_stream(app.stream(inputs, stream_mode="values"))