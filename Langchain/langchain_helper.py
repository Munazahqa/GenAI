from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

#from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from langchain.agents import initialize_agent, AgentType 
from langchain_community.agent_toolkits.load_tools import load_tools

from langchain.agents import initialize_agent
from langchain.agents import AgentType
""""
load_dotenv()
print("API KEY:", os.getenv("OPENAI_API_KEY"))
print("API KEY:", repr(os.getenv("OPENAI_API_KEY")))

print("BASE URL:", os.getenv("OPENAI_API_BASE"))
print("MODEL NAME:", os.getenv("OPENAI_MODEL_NAME"))

def generate_pet_name(animal_type, pet_color):
    llm = ChatOpenAI(
        temperature=0.7,                   
       
        model="openai/gpt-4o",
        base_url="https://openrouter.ai/api/v1",
        openai_api_key="API_key"

    )

    prompt_template_name = PromptTemplate(
        input_variables= ['animal_type', 'pet_color'],
        template="I have a {animal_type} pet and it is {pet_color} in color. I want a cool name for it. Suggest me 3 cool names."
    )


    #chain = LLMChain(llm=llm, prompt=prompt_template_name)
    chain = prompt_template_name | llm
    response = chain.invoke({'animal_type': animal_type, 'pet_color': pet_color})
    return response.content
    #response = llm.invoke("I have a cat pet and I want a cool name for it. Suggest me 3 cool names.")
    #return response.content



def langchain_agent():
    llm = ChatOpenAI(
        temperature=0.7,                   
       
        model="openai/gpt-4o",
        base_url="https://openrouter.ai/api/v1",
        openai_api_key="API_key"

    )


    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose =True 
    )


    result = agent.invoke(
        "What is the average age of a dog? multiple the age by 3"
    )


    print(result)

if __name__ == "__main__":
    langchain_agent()
    #print(generate_pet_name("cow", "black"))



    """





from langchain.document_loaders import YoutubeLoader
from langchain.text_spliter import RecursiveCharacterTextSplitter
from langchain.vertorstores import FAISS




