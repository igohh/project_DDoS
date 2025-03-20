#!/bin/bash

# DDoS Attack Detection and Mitigation - Installation Script
# This script installs all required dependencies and sets up the environment

# Set up colors for output
BLUE='\033[0;34m'
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}=========================================================${NC}"
echo -e "${BLUE}   DDoS Attack Detection and Mitigation - Installation   ${NC}"
echo -e "${BLUE}=========================================================${NC}"
echo ""

# Function to check if a command exists
command_exists() {
    command -v "$1" &> /dev/null
}

# Check Python version
echo -e "${YELLOW}Checking Python version...${NC}"
if command_exists python3; then
    PYTHON_VERSION=$(python3 --version | grep -oP '(?<=Python )\d+\.\d+')
    if (( $(echo "$PYTHON_VERSION >= 3.7" | bc -l) )); then
        echo -e "${GREEN}Python $PYTHON_VERSION detected. Continuing...${NC}"
    else
        echo -e "${RED}Python $PYTHON_VERSION detected. Version 3.7 or higher is required.${NC}"
        exit 1
    fi
else
    echo -e "${RED}Python 3 not found. Please install Python 3.7 or higher.${NC}"
    exit 1
fi

# Check if Git is installed
echo -e "${YELLOW}Checking for Git...${NC}"
if command_exists git; then
    echo -e "${GREEN}Git is installed. Continuing...${NC}"
else
    echo -e "${RED}Git is not installed. Please install Git before continuing.${NC}"
    exit 1
fi

# Check if the repository directory already exists
REPO_DIR="DDoS-Attack-Detection-and-Mitigation"
if [ -d "$REPO_DIR" ]; then
    echo -e "${YELLOW}Repository directory already exists. Checking for updates...${NC}"
    cd "$REPO_DIR"
    git pull
    cd ..
    echo -e "${GREEN}Repository updated successfully.${NC}"
else
    # Clone the repository
    echo -e "${YELLOW}Cloning the repository...${NC}"
    git clone https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation.git
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Repository cloned successfully.${NC}"
    else
        echo -e "${RED}Failed to clone repository. Please check your internet connection and try again.${NC}"
        exit 1
    fi
fi

# Create necessary directories
echo -e "${YELLOW}Creating necessary directories...${NC}"
mkdir -p DDoS-Attack-Detection-and-Mitigation/models
mkdir -p DDoS-Attack-Detection-and-Mitigation/results
echo -e "${GREEN}Directories created.${NC}"

# Install Python dependencies
echo -e "${YELLOW}Installing Python dependencies...${NC}"
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo -e "${GREEN}Dependencies installed successfully.${NC}"
else
    echo -e "${RED}Failed to install some dependencies. The application may not work correctly.${NC}"
    echo -e "${YELLOW}Please check the output above for specific errors.${NC}"
fi

# Setup environment
echo -e "${YELLOW}Setting up environment...${NC}"
# Make run script executable
chmod +x run.sh

# Create environment variables if needed
# (Placeholder for future environment variable setup)

echo -e "${GREEN}Environment setup completed.${NC}"

# Final message
echo -e "${BLUE}===============================================================${NC}"
echo -e "${GREEN}Installation completed successfully!${NC}"
echo -e "To run the application, use: ${YELLOW}./run.sh${NC}"
echo -e "For troubleshooting, refer to ${YELLOW}troubleshoot.md${NC}"
echo -e "${BLUE}===============================================================${NC}"

exit 0