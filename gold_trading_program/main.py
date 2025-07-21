"""
This is the main entry point for the Gold Trading Program.
It initializes the application and starts the user interface.
"""
import sys
import os
from src.ui.dashboard import create_dashboard

# Add the project root to the Python path to allow for absolute imports
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
sys.path.insert(0, project_root)

if __name__ == "__main__":
    # Create and run the dashboard
    create_dashboard()
