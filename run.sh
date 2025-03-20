#!/bin/bash

# DDoS Attack Detection and Mitigation - Run Script
# This script starts the web interface for the DDoS detection tools

# Set up colors for output
BLUE='\033[0;34m'
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}=========================================================${NC}"
echo -e "${BLUE}   DDoS Attack Detection and Mitigation - Starting App   ${NC}"
echo -e "${BLUE}=========================================================${NC}"
echo ""

# Function to check if a command exists
command_exists() {
    command -v "$1" &> /dev/null
}

# Check if Python is installed
if ! command_exists python3; then
    echo -e "${RED}Python 3 not found. Please run the installation script first.${NC}"
    exit 1
fi

# Check if the repository exists
if [ ! -d "DDoS-Attack-Detection-and-Mitigation" ]; then
    echo -e "${RED}Repository not found. Please run the installation script first.${NC}"
    exit 1
fi

echo -e "${YELLOW}Starting DDoS Attack Detection and Mitigation Web Interface...${NC}"
echo -e "${GREEN}The web interface will be available at: http://localhost:5000${NC}"
echo -e "${YELLOW}Press Ctrl+C to stop the server.${NC}"
echo ""

# Start the Flask application
python3 main.py

# Exit with success
exit 0