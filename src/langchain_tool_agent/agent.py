from google.adk.agents import Agent
from  google.adk.tools.langchain_tool import LangchainTool
from dotenv import  load_dotenv #ler as variaveis salvas o .env
import os
import sys
sys.path.append("..")
import google.cloud.logging
from prompt import instrucao

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

load_dotenv()
cloud_logging_client = google.cloud.logging.Client() #cria conexao com google cloud 
cloud_logging_client.setup_logging()


root_agent = Agent(
     name= "langchain_tool_agent",
        model= os.getenv("MODEL"),
        description= "Answers questions using Wikipedia",
        instruction= instrucao,
        tools = [LangchainTool(
            tool=WikipediaQueryRun(api_wrapper= WikipediaAPIWrapper())
        )],
    )