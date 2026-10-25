from google.adk.agents import Agent
from .open_positions_agent import open_positions_agent
from .interview_qa_agent import interview_qa_agent
from .interview_tips_agent import interview_tips_agent


#fluxo de trabalho
interview_prep_pipeline = Agent(
    name= "InterviewPrepPipeline",
    sub_agents= [open_positions_agent, interview_qa_agent, interview_tips_agent], #sequencial
    description= "Sugere vagas de emprego abertas, perguntas e respostas para entrevistas e dicas de preparação, coloque em ordem de numerica (digite 1, 2 ou 3)"
)

root_agent = interview_prep_pipeline
 