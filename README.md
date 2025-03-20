# DDoS Attack Detection and Mitigation - Local Setup

This package provides a simple way to set up and run the [DDoS Attack Detection and Mitigation repository](https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation) locally. The setup scripts handle cloning the repository, installing dependencies, and provide easy execution commands.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.6 or higher
- Git
- pip (Python package manager)

## Quick Start

Follow these steps to quickly set up and run the DDoS Attack Detection system:

1. Download this setup package to your local machine
2. Make the installation script executable and run it:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```
3. Make the run script executable and run the application:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

## What This Package Does

This setup package automates the following tasks:

1. Verifies that Python, Git, and pip are installed on your system
2. Clones the DDoS Attack Detection and Mitigation repository
3. Installs all required dependencies (numpy, pandas, scikit-learn, matplotlib, seaborn, tensorflow, keras)
4. Sets up the necessary directories for storing detection results and models
5. Provides a simple run script to execute the DDoS detection system

## System Requirements

- Operating System: Windows, macOS, or Linux
- Python: Version 3.6 or higher (3.8+ recommended)
- RAM: At least 4GB (8GB recommended for larger datasets)
- Disk Space: At least 1GB for the repository, dependencies, and datasets

## Manual Installation Steps

If the automatic installation script doesn't work for you, follow these manual steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation.git
   ```
2. Install the required dependencies:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn tensorflow keras
   ```
3. Create directories for results and models:
   ```bash
   mkdir -p DDoS-Attack-Detection-and-Mitigation/results
   mkdir -p DDoS-Attack-Detection-and-Mitigation/models
   ```
4. Run the application:
   ```bash
   cd DDoS-Attack-Detection-and-Mitigation
   python main.py
   ```

## Troubleshooting

If you encounter any issues during setup or execution, refer to the troubleshoot.md file for common problems and their solutions.
   