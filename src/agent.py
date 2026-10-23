from google.adk.agents import Agent
from google.adk.tools import google_search
from google.genai import types
from src.prompt import instrucao

def morning_greet(name: str) -> str:
    return f"Bom dia, {name}! Que tal uma recomendação de filme para começar bem o dia?"

def evening_greet(name: str) -> str:
    return f"Boa noite, {name}! Que tal relaxar com um bom filme antes de dormir?"


root_agent = Agent(
    name= "my_first_agent",
    model= "gemini-3.5-flash-lite",
    generate_content_config=types.GenerateContentConfig(
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(initial_delay=1, attempts=3),
        ),
    ),
    description= "Assistente prático de cinema focado em filmes. Recomenda apenas um título por vez e avalia com uma opinião sincera qualquer filme citado pelo usuário, sem spoilers e sem enrolação.",
    instruction= instrucao,
    #tools = [google_search],) # Pode utilizar a pesquisa no google para melhorar a experiencia do usuario em questoes de filmes.
)