# Troubleshooting Guide

This document provides solutions to common issues you might encounter when setting up and running the DDoS Attack Detection and Mitigation repository.

## Installation Issues

### Error: Python version not compatible

**Problem**: Setup fails with a message indicating Python version is not compatible.

**Solution**:
1. Check your Python version:
   ```bash
   python --version
   ```
2. If the version is below 3.6, install a newer version:
   - On Ubuntu/Debian:
     ```bash
     sudo apt update
     sudo apt install python3.8
     ```
   - On macOS:
     ```bash
     brew install python@3.8
     ```
   - On Windows: Download the installer from [python.org](https://www.python.org/downloads/)

### Error: Git not found

**Problem**: The setup script cannot find Git.

**Solution**:
1. Install Git:
   - On Ubuntu/Debian:
     ```bash
     sudo apt update
     sudo apt install git
     ```
   - On macOS:
     ```bash
     brew install git
     ```
   - On Windows: Download the installer from [git-scm.com](https://git-scm.com/downloads)

### Error: pip command not found

**Problem**: The setup script cannot find pip.

**Solution**:
1. Install pip:
   - On Ubuntu/Debian:
     ```bash
     sudo apt update
     sudo apt install python3-pip
     ```
   - On macOS:
     ```bash
     python3 -m ensurepip --upgrade
     ```
   - On Windows: Pip should be installed with Python automatically

### Error: Permission denied when running .sh files

**Problem**: You cannot execute the installation or run scripts.

**Solution**:
1. Make the scripts executable:
   ```bash
   chmod +x install.sh run.sh
   ```

## Dependency Issues

### Error: Failed to install dependencies

**Problem**: The dependency installation fails with error messages.

**Solution**:
1. Try updating pip:
   ```bash
   python -m pip install --upgrade pip
   ```
2. Install dependencies manually:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn tensorflow keras
   ```
3. If specific packages fail, check for system dependencies:
   - On Ubuntu/Debian:
     ```bash
     sudo apt install python3-dev build-essential
     ```

### Error: Import errors when running the application

**Problem**: The application fails with import errors.

**Solution**:
1. Ensure you're using the virtual environment:
   ```bash
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
2. Verify dependencies are installed:
   ```bash
   pip list
   ```
3. Reinstall the missing package:
   ```bash
   pip install packagename
   ```

## Runtime Issues

### Error: FileNotFoundError when accessing dataset

**Problem**: The application cannot find dataset files.

**Solution**:
1. Verify the dataset directory exists:
   ```bash
   ls DDoS-Attack-Detection-and-Mitigation/dataset
   ```
2. If not, re-run the setup script:
   ```bash
   python setup.py
   