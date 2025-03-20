#!/bin/bash
# Run script for DDoS Attack Detection and Mitigation
# This script runs the application without needing a virtual environment

set -e  # Exit on any error

# Print colored messages
print_message() {
    GREEN='\033[0;32m'
    NC='\033[0m' # No Color
    echo -e "${GREEN}$1${NC}"
}

print_error() {
    RED='\033[0;31m'
    NC='\033[0m' # No Color
    echo -e "${RED}$1${NC}"
}

# Check if Python is available
check_python() {
    print_message "Checking Python..."
    
    if command -v python3 >/dev/null 2>&1; then
        PYTHON_CMD=python3
    elif command -v python >/dev/null 2>&1; then
        PYTHON_CMD=python
    else
        print_error "Python is not installed. Please install Python 3.6+ and try again."
        exit 1
    fi
    
    print_message "Python is available - OK"
}

# Check if repository exists
check_repo() {
    print_message "Checking repository..."
    
    if [ ! -d "DDoS-Attack-Detection-and-Mitigation" ]; then
        print_error "Repository not found. Have you run the install.sh script?"
        exit 1
    fi
    
    print_message "Repository found - OK"
}

# Run the application
run_application() {
    print_message "Running DDoS Attack Detection and Mitigation application..."
    
    cd DDoS-Attack-Detection-and-Mitigation
    
    # Check if main.py exists
    if [ ! -f "main.py" ]; then
        print_error "main.py not found. Repository structure may have changed."
        exit 1
    fi
    
    print_message "Starting the application..."
    $PYTHON_CMD main.py
    
    cd ..
}

# Main function
main() {
    print_message "==============================================================="
    print_message "  DDoS Attack Detection and Mitigation - Run Script"
    print_message "==============================================================="
    
    check_python
    check_repo
    run_application
    
    print_message "==============================================================="
    print_message "Application execution completed."
    print_message "==============================================================="
}

# Run the main function
main
