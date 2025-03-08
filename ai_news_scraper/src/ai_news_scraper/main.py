#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from ai_news_scraper.crew import AiNewsScraper

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew with dynamic topic input from the terminal.
    """
    topic = input("Please enter the topic to scrape (e.g., 'AI LLMs'): ").strip()
    if not topic:
        print("No topic provided. Using default topic 'AI LLMs'.")
        topic = 'AI LLMs'

    date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    inputs = {
        'topic': topic,
        'date': date
    }

    try:
        AiNewsScraper().crew().kickoff(inputs=inputs)
    except Exception as e:
        print(f"An error occurred while running the crew: {e}")
        sys.exit(1)  # Exit with error code if an exception occurs

    sys.exit(0)  # Exit successfully after execution

if __name__ == "__main__":
    run()
