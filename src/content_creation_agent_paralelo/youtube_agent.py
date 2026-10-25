from google.adk.agents import Agent
from dotenv import load_dotenv
import os


load_dotenv()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

youtube_agent = Agent(
    name= "YoutubeAgent",
    model = GEMINI_MODEL,
    instruction= """Você é um estrategista de conteúdo para o YouTube. Cria:

1. Um título apelativo
2. Um guião de vídeo (curto, conversacional, leitura < 2 min)
3. Uma descrição para o YouTube (otimizada para SEO, com 3-4 palavras-chave)

para o tópico com base na consulta do utilizador.""",

    output_key= "youtube_content",
    
)