from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import warnings

load_dotenv()

warnings.filterwarnings('ignore')

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class WriteArticle():
	"""WriteArticle crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def planner(self) -> Agent:
		return Agent(
			config=self.agents_config['planner'],
			allow_delegation=False,
			verbose=True
		)

	@agent
	def writer(self) -> Agent:
		return Agent(
			config=self.agents_config['writer'],
			allow_delegation=False,
			verbose=True
		)
	
	@agent
	def editor(self) -> Agent:
		return Agent(
			config=self.agents_config['editor'],
			allow_delegation=False,
			verbose=True
		)


	@task
	def planner_task(self) -> Task:
		return Task(
			config=self.tasks_config['planner_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['writer_task'],
			output_file='report.md'
		)
	
	@task
	def editor_task(self) -> Task:
		return Task(
			config=self.tasks_config['editor_task'],
			output_file='report.md'
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the WriteArticle crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
 