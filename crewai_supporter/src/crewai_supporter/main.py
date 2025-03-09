#!/usr/bin/env python
import sys
import warnings
from crewai_supporter.crew import Support_Crew  # Importing crew from crew.py

warnings.filterwarnings("ignore", category=SyntaxWarning)

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information.

def run():
    """
    Run the crew.
    """
    inputs = {
        "customer": "NexisAI",
        "person": "Abdul Raqeeb",
        "inquiry": "I need help with setting up a Crew "
                   "and kicking it off, specifically "
                   "how can I add memory to my crew? "
                   "Can you provide guidance?"
    }
    
    try:
        Support_Crew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
run()
