# DDoS Attack Detection and Mitigation

A comprehensive package for detecting and mitigating Distributed Denial of Service (DDoS) attacks using machine learning algorithms.

## Overview

This package provides a user-friendly web interface for interacting with the [DDoS-Attack-Detection-and-Mitigation](https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation) repository. It enables users to detect and mitigate DDoS attacks using various machine learning algorithms and defense strategies.

![Dashboard Screenshot](static/images/dashboard.png)

## Features

- **Multiple ML Algorithms**: Support for 6 different machine learning algorithms (LR, KNN, SVM, NB, DT, RF)
- **Interactive Dashboard**: Visualize detection results and attack statistics
- **Mitigation Strategies**: Implement various defense mechanisms against detected attacks
- **User-Friendly Interface**: Simple web interface for interacting with detection and mitigation tools
- **Comprehensive Documentation**: Detailed guides for installation, usage, and troubleshooting

## Quick Start

### Prerequisites

- Python 3.7 or higher
- Git
- pip (Python package manager)

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ddos-detection-package.git
   cd ddos-detection-package
   ```

2. Run the installation script:
   ```
   chmod +x install.sh
   ./install.sh
   ```
   
   The installation script will:
   - Check Python and Git installation
   - Clone the DDoS-Attack-Detection-and-Mitigation repository
   - Install required dependencies
   - Set up the environment

3. Start the application:
   ```
   ./run.sh
   ```

4. Open your web browser and navigate to: `http://localhost:5000`

## Usage

### Detection

1. Navigate to the Detection page
2. Select a machine learning algorithm
3. Run the detection
4. View and analyze the results

### Mitigation

1. Navigate to the Mitigation page
2. Choose a mitigation strategy
3. Configure settings based on your network
4. Apply the mitigation
5. Monitor its effectiveness

## Machine Learning Algorithms

- **Logistic Regression (LR)**: Fast and efficient for binary classification
- **K-Nearest Neighbors (KNN)**: Classifies based on distance metrics
- **Support Vector Machine (SVM)**: Effective for complex, non-linear decision boundaries
- **Naive Bayes (NB)**: Probabilistic approach with good performance on small datasets
- **Decision Tree (DT)**: Rule-based classification with clear decision logic
- **Random Forest (RF)**: Ensemble method with high accuracy and robustness

## Mitigation Strategies

- **Rate Limiting**: Restricts the number of requests per time period
- **Connection Limiting**: Controls concurrent connections from a source
- **IP Blocking**: Blocks traffic from identified malicious IPs
- **Traffic Filtering**: Analyzes and filters traffic based on patterns
- **CAPTCHA Challenge**: Verifies human users during suspected attacks

## Directory Structure

```
.
├── DDoS-Attack-Detection-and-Mitigation/ (Cloned repository)
│   ├── Codes/                           (Core detection and mitigation code)
│   ├── Certificate/                     (Project certificates)
│   ├── Installation_setup/              (Original setup files)
│   ├── models/                          (Trained ML models)
│   └── results/                         (Detection results)
├── static/                              (Web assets)
│   ├── css/                             (Stylesheets)
│   └── js/                              (JavaScript files)
├── templates/                           (HTML templates)
├── install.sh                           (Installation script)
├── run.sh                               (Execution script)
├── main.py                              (Flask application)
└── troubleshoot.md                      (Troubleshooting guide)
```

## Troubleshooting

If you encounter issues during installation or execution, please refer to the [troubleshooting guide](troubleshoot.md).

## License

This project is distributed under the MIT License. See the [LICENSE](DDoS-Attack-Detection-and-Mitigation/LICENSE) file for more details.

## Acknowledgments

- Original repository by [Chirag Biradar](https://github.com/chiragbiradar)
- Built on research in machine learning approaches to network security
- Utilizes various open-source libraries and tools

## Security Notice

This tool is designed for educational and defensive purposes only. Always ensure you have proper authorization before deploying in any network environment.