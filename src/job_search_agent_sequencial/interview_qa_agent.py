from google.adk.agents import Agent
from dotenv import load_dotenv
import os
from .open_positions_agent import open_positions_agent

load_dotenv()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")


interview_qa_agent = Agent(
    name= "INterviewQAAgent",
    model = GEMINI_MODEL,
    instruction= f"""És um treinador de entrevistas (interview coach). Com base na consulta fornecida e consultando {{open_positions}}, 
    cria 5 perguntas comuns de entrevista com exemplos de respostas consistentes.
 
 Formato:
P: <pergunta>
R: <resposta>""",
    output_key= "interview_qa",

)