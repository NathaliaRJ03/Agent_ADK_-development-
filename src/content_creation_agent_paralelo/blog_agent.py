from google.adk.agents import Agent
from dotenv import load_dotenv
import os


load_dotenv()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

blog_agent = Agent(
    name= "BlogAgent",
    model = GEMINI_MODEL,
    instruction= """"Você é um especialista em blogs. Sugere uma estrutura envolvente para um artigo de blog e ideias de conteúdo 
    sobre o tópico com base na consulta do utilizador."

    Formato de saída:
    - Título Sugerido
    - Estrutura do Blog (3 a 5 cabeçalhos)
    - Pontos-chave sob cada cabeçalho """,

    output_key = "blog_content"

    
)