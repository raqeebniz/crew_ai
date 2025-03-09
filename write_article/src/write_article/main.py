#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from write_article.crew import WriteArticle

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def get_user_topic():
    """
    Prompt the user to enter a topic for the article.
    """
    while True:
        topic = input("Please enter the topic for the article: ").strip()
        if topic:
            return topic
        print("Topic cannot be empty. Please try again.")

def run():
    """
    Run the crew with user-provided topic.
    """
    # Get topic from user after execution starts
    topic = get_user_topic()
    
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }
    
    try:
        WriteArticle().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()