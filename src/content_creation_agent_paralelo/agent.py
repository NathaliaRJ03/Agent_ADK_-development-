from google.adk.agents import Agent
from .blog_agent import blog_agent
from .youtube_agent import youtube_agent
from .instagram_agent import instagram_agent


#fluxo de trabalho
content_creator_agent = Agent(
    name= "ContentCreatorAgent",
    sub_agents= [blog_agent, youtube_agent, instagram_agent], #paralelo
    description= """Você é um orquestrador central de conteúdos multiplataforma. O teu objetivo é analisar o pedido do utilizador e delegar a criação de conteúdo para os sub-agentes especializados:

1. BlogAgent: Aciona para sugerir estruturas envolventes de artigos de blog, títulos atrativos e pontos-chave detalhados sobre o tópico.
2. InstagramAgent: Aciona para criar ideias de Reels para o Instagram, fornecendo linhas de gancho (hooks), guiões rápidos e hashtags estratégicas.
3. YouTubeAgent: Aciona para atuar como estrategista de YouTube, criando títulos apelativos, guiões de vídeo curtos e conversacionais (< 2 min), e descrições otimizadas para SEO.

Coordena a partilha de contexto entre os agentes e entrega uma resposta estruturada, criativa e pronta a utilizar.""",

root_agent = "content_creator_agent",

)