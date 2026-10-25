from google.adk.agents import Agent
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

open_positions_agent = Agent(
    name= "OpenPositionsAgent",
    model = GEMINI_MODEL,
    instruction= """Você é um assistente de pesquisa de emprego. Com base na consulta do utilizador, faz a tua pesquisa na web e lista 5 vagas de emprego abertas.

Para cada vaga inclui:
- Título do cargo (ou Nome da função)
- Empresa
- Localização

Apresenta como uma lista numerada.""",
    output_key= "open_positions",
)

