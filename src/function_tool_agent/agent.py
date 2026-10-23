from google.adk.agents import Agent
import requests
import json
import sys
from dotenv import load_dotenv
import os
from prompt import instrucao

load_dotenv()



GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def github_create_repo_tool(repo_name:str, description: str = "" , private: bool = True):
    """
        Cria um novo repositório no GitHub.

        Esta função utiliza a API do GitHub para criar um novo repositório na
        conta de usuário especificada. Requer um nome de usuário do GitHub e um
        Personal Access Token com o escopo 'repo'.

         Args:
        repo_name (str): O nome do novo repositório.
        description (str): Uma breve descrição do repositório. O padrão é "".
        private (bool): Se True, cria um repositório privado. O padrão é True.
    """


    def github_delete_repo_tool(repo_name: str):
        """ 
        Elimina um repositório no GitHub.

        Esta função utiliza a API do GitHub para eliminar um repositório. Esta ação
        é irreversível e deve ser utilizada com cautela.

        Args:
        repo_name (str): O nome do repositório a eliminar.
        """

    if not GITHUB_USERNAME:
        print("Erro: Nome de utilizador do GitHub não encontrado. Por favor, defina a variável de ambiente GITHUB_USERNAME.")
        return

    if not GITHUB_TOKEN:
        print("Erro: Token do GitHub não encontrado. Por favor, defina a variável de ambiente GITHUB_TOKEN.")
        return


    #root_agent = Agent(
        name= "github_repo_agent"
        model= "gemini-3.5-flash-lite",
        description= "Agente de criar e deletar github repositorio.",
        instruction= instrucao,
        tools= [github_create_repo_tool, github_delete_repo_tool]
    #)


