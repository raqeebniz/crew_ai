
from research_agent.crews.research_agent.agent import LatestAiDevelopmentCrew


def main():
    crew = LatestAiDevelopmentCrew().crew()  # Instantiate and get the crew
    result = crew.kickoff()  # Start the crew's tasks
    print("Final Result:", result)