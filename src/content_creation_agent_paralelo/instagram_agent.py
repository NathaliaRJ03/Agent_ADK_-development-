from google.adk.agents import Agent
from dotenv import load_dotenv
import os


load_dotenv()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

instagram_agent = Agent(
    name= "InstagramAgent",
    model = GEMINI_MODEL,
    instruction= """Voce é um criador de conteúdo para redes sociais. Sugere 3 ideias de Reels para o Instagram para o tópico com base [na consulta do utilizador].

    Para cada reel, fornece:
    - Linha de gancho (Hook line)
    - Ideia rápida de guião
    - Hashtags sugeridas" """,

    output_key= "instagram_content",

    
)