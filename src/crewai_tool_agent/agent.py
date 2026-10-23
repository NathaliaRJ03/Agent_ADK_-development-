from google.adk.agents import Agent
from dotenv import  load_dotenv #ler as variaveis salvas o .env
from google.genai import types
import os
import sys
sys.path.append("..")
import google.cloud.logging
from prompt import instrucao
from crewai_tools import ScrapeWebsiteTool
from google.adk.integrations.crewai import CrewaiTool



load_dotenv()

cloud_logging_client = google.cloud.logging.Client() #cria conexao com google cloud 
cloud_logging_client.setup_logging()


root_agent = Agent(
    name= "crewai_tool_agent",
    model= os.getenv("MODEL"),
    description= "Agent to write files.",
    instruction= instrucao,
    generate_content_config= types.GenerateContentConfig(
            temperature=0
    ),

    tools = [
        CrewaiTool(
            name = "check_google_cloud_release_notes",
            description= ("""Raspa as últimas mudanças do Google Cloud na página oficial de notas de lançamento do Google Cloud.
              Use esta ferramenta para ficar por dentro das novidades sobre produtos e serviços do Google Cloud."""
            ),
            tool = ScrapeWebsiteTool("")
        )
    ]
)



