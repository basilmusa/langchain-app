import os
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate
)
from langchain.schema import SystemMessage, HumanMessage

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

# Langchain OpenAI Client
chat = ChatOpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY'])

# messages
messages = [
    SystemMessage(
        content="You are a helpful assistant that translates English to French."
    ),
    HumanMessage(
        content="Translate this sentence from English to French. I love programming."
    ),
]

response = chat.invoke(messages)

print(response)
