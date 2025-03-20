#!/bin/bash
# Installation script for DDoS Attack Detection and Mitigation
# This script automates the setup process

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

# Check for Python 3.6+
check_python() {
    print_message "Checking Python version..."
    if command -v python3 >/dev/null 2>&1; then
        PYTHON_CMD=python3
    elif command -v python >/dev/null 2>&1; then
        PYTHON_CMD=python
    else
        print_error "Python is not installed. Please install Python 3.6+ and try again."
        exit 1
    fi

    PYTHON_VERSION=$($PYTHON_CMD -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

    if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 6 ]); then
        print_error "Python 3.6+ is required. Current version: $PYTHON_VERSION"
        exit 1
    fi
    
    print_message "Python $PYTHON_VERSION detected - OK"
}

# Check for git
check_git() {
    print_message "Checking for Git..."
    if ! command -v git >/dev/null 2>&1; then
        print_error "Git is not installed. Please install Git and try again."
        exit 1
    fi
    print_message "Git is installed - OK"
}

# Check for pip
check_pip() {
    print_message "Checking for pip..."
    if ! $PYTHON_CMD -m pip --version >/dev/null 2>&1; then
        print_error "pip is not installed. Please install pip and try again."
        exit 1
    fi
    print_message "pip is installed - OK"
}

# Clone repository
clone_repository() {
    print_message "Cloning repository..."
    REPO_URL="https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation.git"
    REPO_DIR="DDoS-Attack-Detection-and-Mitigation"
    
    if [ -d "$REPO_DIR" ]; then
        print_message "Repository directory already exists."
        print_message "Using existing repository directory."
    else
        print_message "Cloning repository from $REPO_URL"
        git clone $REPO_URL
        print_message "Repository cloned successfully."
    fi
}

# Install dependencies directly (without virtual env for Replit)
install_dependencies() {
    print_message "Installing dependencies..."
    
    # These are the dependencies required by the repository
    $PYTHON_CMD -m pip install numpy pandas scikit-learn matplotlib seaborn tensorflow keras flask
    
    print_message "Dependencies installed successfully."
}

# Create necessary directories
setup_environment() {
    print_message "Setting up environment..."
    
    REPO_DIR="DDoS-Attack-Detection-and-Mitigation"
    
    # Creating directories for storing detection results if they don't exist
    mkdir -p "$REPO_DIR/results"
    mkdir -p "$REPO_DIR/models"
    
    print_message "Environment setup completed."
}

# Main installation process
main() {
    print_message "==============================================================="
    print_message "  DDoS Attack Detection and Mitigation - Installation Script"
    print_message "==============================================================="
    
    check_python
    check_git
    check_pip
    clone_repository
    install_dependencies
    setup_environment
    
    print_message "==============================================================="
    print_message "Installation completed successfully!"
    print_message "To run the application, use: ./run.sh"
    print_message "For troubleshooting, refer to troubleshoot.md"
    print_message "==============================================================="
}

# Run the main function
main
