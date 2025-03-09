from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool
from dotenv import load_dotenv
import warnings
import os

load_dotenv()
warnings.filterwarnings('ignore')


search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

docs_scrape_tool = ScrapeWebsiteTool(
    website_url=["https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/",
                 "https://docs.crewai.com/concepts/memory"]
)



@CrewBase
class Support_Crew():
    """AiNewsScraper crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def support_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['support_agent'],
            allow_delegation=False,
            verbose=True
        )

    @agent
    def support_quality_assurance_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['support_quality_assurance_agent'],
            verbose=True
        )

  
    @task
    def inquiry_resolution_task(self) -> Task:
        return Task(
            config=self.tasks_config['inquiry_resolution_task'],
            tools=[docs_scrape_tool]
        )

    @task
    def quality_assurance_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['quality_assurance_review_task'],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the AiNewsScraper crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
