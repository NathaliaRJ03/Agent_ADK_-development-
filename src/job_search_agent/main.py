import asyncio
from job_search_agent.agent import root_agent  

async def main():
    user_query = "Gostava de me preparar para vagas de Python Developer no Porto."

    print(f"--- A processar o pedido: '{user_query}' ---\n")

    response = await root_agent.run_async(user_query) # await= aguarda a execução do agente root_agent com a consulta .

    print("--- Resultado Final ---")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())