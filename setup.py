#!/usr/bin/env python3
"""
Setup script for DDoS Attack Detection repository.
This script will clone the repository and set up the environment.
"""

import os
import sys
import subprocess
import platform
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

REPO_URL = "https://github.com/chiragbiradar/DDoS-Attack-Detection.git"
REPO_DIR = "DDoS-Attack-Detection"

def check_python_version():
    """Check if Python version is compatible."""
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 6):
        logger.error("Python 3.6+ is required. Current version: %s.%s", 
                    python_version.major, python_version.minor)
        sys.exit(1)
    logger.info("Python version: %s.%s - OK", python_version.major, python_version.minor)

def check_git():
    """Check if git is installed."""
    try:
        subprocess.run(["git", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info("Git is installed - OK")
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        logger.error("Git is not installed. Please install Git and try again.")
        return False

def check_pip():
    """Check if pip is installed."""
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], 
                      check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info("pip is installed - OK")
        return True
    except subprocess.SubprocessError:
        logger.error("pip is not installed. Please install pip and try again.")
        return False

def clone_repository():
    """Clone the repository."""
    if os.path.exists(REPO_DIR):
        logger.info("Repository directory already exists.")
        choice = input(f"Do you want to remove the existing {REPO_DIR} directory and clone again? (y/n): ")
        if choice.lower() == 'y':
            import shutil
            shutil.rmtree(REPO_DIR)
        else:
            logger.info("Using existing repository directory.")
            return

    logger.info("Cloning repository from %s", REPO_URL)
    try:
        subprocess.run(["git", "clone", REPO_URL], check=True)
        logger.info("Repository cloned successfully.")
    except subprocess.SubprocessError as e:
        logger.error("Failed to clone repository: %s", e)
        sys.exit(1)

def install_dependencies():
    """Install required dependencies."""
    logger.info("Installing required dependencies...")
    requirements_path = os.path.join(os.getcwd(), "requirements.txt")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], check=True)
        logger.info("Dependencies installed successfully.")
    except subprocess.SubprocessError as e:
        logger.error("Failed to install dependencies: %s", e)
        sys.exit(1)

def setup_environment():
    """Set up any additional environment configurations."""
    logger.info("Setting up environment...")
    
    # Creating directories for storing detection results if they don't exist
    repo_path = Path(REPO_DIR)
    results_dir = repo_path / "results"
    models_dir = repo_path / "models"
    
    results_dir.mkdir(exist_ok=True)
    models_dir.mkdir(exist_ok=True)
    
    logger.info("Environment setup completed.")

def validate_setup():
    """Validate the setup by checking essential files."""
    logger.info("Validating setup...")
    
    essential_files = [
        os.path.join(REPO_DIR, "main.py"),
        os.path.join(REPO_DIR, "dataset", "Friday-WorkingHours-Morning.pcap_ISCX.csv")
    ]
    
    missing_files = [f for f in essential_files if not os.path.exists(f)]
    
    if missing_files:
        logger.warning("Some essential files are missing:")
        for file in missing_files:
            logger.warning("  - %s", file)
        logger.warning("The setup may not be complete. Please check the repository.")
    else:
        logger.info("All essential files are present.")

def main():
    """Main function to run the setup."""
    logger.info("Starting setup for DDoS Attack Detection...")
    
    # Check prerequisites
    check_python_version()
    if not check_git() or not check_pip():
        sys.exit(1)
    
    # Clone repository and setup
    clone_repository()
    install_dependencies()
    setup_environment()
    validate_setup()
    
    logger.info("""
    =================================================================
    Setup completed successfully!
    
    To run the DDoS detection system:
      1. Navigate to the repository directory: cd %s
      2. Run the main script: python main.py
    
    For more information, refer to the README.md and documentation.
    If you encounter any issues, check troubleshoot.md for solutions.
    =================================================================
    """, REPO_DIR)

if __name__ == "__main__":
    main()
