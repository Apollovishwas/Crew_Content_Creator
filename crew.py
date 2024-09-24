import os
import sys
from crewai import Crew, Process
import agentops
from langsmith import trace

from langchain_community.llms import Ollama

from langchain_openai import ChatOpenAI
from agents import Trend_researcher, Hashtag_Specialist, Caption_Generator, Email_Content_Generator
from task import research_task, summarize_and_hashtag_task, caption_task, email_newsletter_task
# ollama_llm = Ollama(model="phi3")




##Setup
#agentops.init("c66129a4-58dc-456e-b85e-c935b3619e80")
os.environ["OPENAI_API_KEY"] = ""
os.environ["SERPER_API_KEY"] = ""
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = ""
##Setup





##Exposing crew to other files
Social_crew = Crew(
        agents=[Trend_researcher, Hashtag_Specialist, Caption_Generator, Email_Content_Generator],
        tasks=[research_task, summarize_and_hashtag_task,caption_task, email_newsletter_task],
        process=Process.sequential,
    )

# def call_crew(desc):
#     with trace("CrewAI Execution", project_name="Product Launcher") as root_run:
#         result = Social_crew.kickoff(inputs={'description': desc})
#         root_run.end(outputs={"result": result})
#     return result

if __name__ == "__main__":
    # This block is only executed if the script is run directly

    print("Social Crew main file")
    sys.exit()