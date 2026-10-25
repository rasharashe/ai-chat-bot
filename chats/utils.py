from langchain_openai import ChatOpenAI 
from openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv('API_KEY')
API_BASE_URL = os.getenv('API_BASE_URL')
AI_MODEL = os.getenv('AI_MODEL')


llm = ChatOpenAI(model=AI_MODEL, openai_api_key=API_KEY, base_url=API_BASE_URL)

system_prompt = SystemMessage(content="You are a helpful assistant.")

def generate_response(user_input, history):
    history_msgs = []

    for msg in history:
        if msg.sender == 'human':
            history_msgs.append(HumanMessage(content=msg.text))
        elif msg.sender == 'ai':
            history_msgs.append(AIMessage(content=msg.text))

    history_msgs.append(HumanMessage(content=user_input))

    prompt = ChatPromptTemplate.from_messages([system_prompt] + history_msgs)
    chain = prompt | llm | StrOutputParser()

    return chain.invoke({})