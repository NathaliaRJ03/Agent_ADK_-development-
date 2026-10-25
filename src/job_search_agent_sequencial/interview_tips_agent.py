from google.adk.agents import Agent
from dotenv import load_dotenv
import os
from .interview_qa_agent import interview_qa_agent
from .open_positions_agent import open_positions_agent

load_dotenv()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

interview_tips_agent = Agent(
    name= "InterviewTipsAgent",
    model = GEMINI_MODEL,
    instruction= f"""Você um mentor de carreira. Fornece dicas e truques práticos para ter excelente desempenho em entrevistas com base no pedido do utilizador. 
    Usa {{open_positions}} para adaptar os teus conselhos. Aconselha também sobre {{interview_qa}}.

Aborda:
- Como pesquisar a empresa
- O que preparar a nível técnico
- Estratégias para entrevistas comportamentais
- Dicas de linguagem corporal e comunicação """,

    output_key= "interview_tips",
)