from crewai_tools import SerperDevTool


#configuring Serpertool
research_tool = SerperDevTool(
    search_url="https://google.serper.dev/search",
    n_results=2,
)