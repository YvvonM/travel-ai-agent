## importing libraries
import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.graph import MermaidDrawMethod
from langchain_groq import ChatGroq
from IPython.display  import display, Image
import gradio as gr

load_dotenv()

#Creating the agent class
class PlannerState(TypedDict):
    messages = Annotated[List[HumanMessage | AIMessage], "the message in the conversation"]
    city: str
    interests: List[str]
    itinerary: str

#define the llm
llm = ChatGroq(
    temperature = 0,
    groq_api_key = os.getenv('GROQ_API_KEY'),
    model_name = 'llama-3.3-70b-versatile'
)

#creating the prompt 
itinerary_promp = ChatPromptTemplate.from_messages([
    ("system","You are a helpful travel assistant. Create a day trip itinerary for {city} based on the user's interests: {interests}. Provide a bulleted itinerary."),
    ("human","Create an itinerary for my day trip."),
])

## the input city function
def input_city(city: str, state: PlannerState) -> PlannerState:
    return {
        **state,
        'city': city,
        'messages': state.get('messages', []) + [HumanMessage(content=city)]
    }

# the input interests function
def input_interest(interests: str, state: PlannerState) -> PlannerState:
    return {
        **state,
        'interests': [interest.strip() for interest in interests.split(',')],
        'messages': state.get('messages', []) + [HumanMessage(content=interests)]
    }

def create_itinerary(state: PlannerState) -> PlannerState:
    print(f"Creating an itinerary for {state['city']} based on interests: {','.join(state['interests'])}")
    # Invoking the llm
    response = llm.invoke(itinerary_promp.format_messages(city=state['city'], interests=', '.join(state['interests'])))
    # Printing the itinerary
    print('\nFinal itinerary:')
    print(response.content)
    return {
        **state,
        'messages': state.get('messages', []) + [HumanMessage(content=response.content)],
        'itinerary': response.content
    }

#defining the gradio application
def travel_planner(city:str, interests:str):
    #initiate the state
    state = {
        'messages':[],
        'city': "",
        'interests': [],
        'itinerary': ""
    }
    #process the city and interests input
    state = input_city(city, state)
    state = input_interest(interests, state)

    #generate the itinerary
    itinerary = create_itinerary(state)
    return itinerary

# Build the Gradio interface
interface = gr.Interface(
    fn=travel_planner,
    theme='Yntec/HaleyCH_Theme_Orange_Green',
    inputs=[
        gr.Textbox(label="Enter the city for your day trip"),
        gr.Textbox(label="Enter your interests (comma-separated)"),
    ],
    outputs=gr.Textbox(label="Generated Itinerary"),
    title="Travel Itinerary Planner",
    description="Enter a city and your interests to generate a personalized day trip itinerary."
)

# Launch the Gradio application
interface.launch()
