from google.adk.agents import Agent
import google.auth
from google.adk.tools import google_search
from google.adk.tools.bigquery import BigQueryCredentialsConfig
from google.adk.tools.bigquery import BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig
from google.adk.tools.bigquery.config import WriteMode
from google.genai import types
from prompt import instrucao
tool_config = BigQueryToolConfig(write_mode=WriteMode.BLOCKED) # ler os dados do banco




application_default_credenciais = google.auth.default()
credentials_config = BigQueryCredentialsConfig(
    credentials = application_default_credenciais
    
)

root_agent = Agent(
    name= "BigQuery_Agent",
    model= "gemini-3.5-flash-lite",
    description= "Agent to answer questions about BigQuery data and models and execute.",
    instruction= instrucao,
    tools = [BigQueryToolset],
)