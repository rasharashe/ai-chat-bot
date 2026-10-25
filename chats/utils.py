from langchain_openai import ChatOpenAI 
from openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv

load_dotenv()

# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

# llm = ChatOpenAI(model='gpt-4o-mini', openai_api_key=OPENAI_API_KEY)
llm = ChatOpenAI(model='gpt-4o-mini', openai_api_key=OPENROUTER_API_KEY, base_url="https://openrouter.ai/api/v1")
# llm = OpenAI(
#   base_url="https://openrouter.ai/api/v1",
#   api_key=OPENROUTER_API_KEY,
# )

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