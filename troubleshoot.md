# DDoS Attack Detection and Mitigation - Troubleshooting Guide

This document provides solutions for common issues that may occur while setting up and running the DDoS Attack Detection and Mitigation system.

## Installation Issues

### Python Version Errors

**Issue**: Error message about Python version requirements.

**Solution**:
- Ensure you have Python 3.7 or higher installed.
- Check your Python version with: `python3 --version`
- If needed, install a newer Python version from [python.org](https://www.python.org/downloads/) or use your operating system's package manager.

### Git Not Found

**Issue**: Installation script reports that Git is not installed.

**Solution**:
- Install Git from [git-scm.com](https://git-scm.com/downloads) or use your operating system's package manager.
- For Ubuntu/Debian: `sudo apt-get install git`
- For macOS (using Homebrew): `brew install git`
- For Windows: Download and install from the official website.

### Repository Clone Failure

**Issue**: Unable to clone the GitHub repository.

**Solution**:
- Check your internet connection.
- Ensure GitHub is accessible from your network.
- Try cloning manually: `git clone https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation.git`
- If you're behind a proxy, configure Git to use it: `git config --global http.proxy http://proxyuser:proxypwd@proxy.server.com:8080`

### Dependency Installation Failures

**Issue**: Python packages fail to install.

**Solution**:
- Ensure pip is up to date: `python3 -m pip install --upgrade pip`
- Try installing dependencies manually: `python3 -m pip install -r requirements.txt`
- If specific packages fail, try installing them individually.
- For system-level dependencies, ensure you have the required build tools installed.

## Runtime Issues

### Web Interface Not Starting

**Issue**: The Flask application doesn't start or shows errors.

**Solution**:
- Check if Python is properly installed: `python3 --version`
- Verify that all dependencies are installed: `python3 -m pip list`
- Check for error messages when starting the application.
- Ensure port 5000 is not in use by another application.

### Algorithm Errors

**Issue**: Machine learning algorithms fail to run.

**Solution**:
- Verify that scikit-learn, TensorFlow, and other ML libraries are properly installed.
- Check if the model directories exist and have proper permissions.
- Ensure Python can access the required modules (check import paths).
- Look for specific error messages that might indicate the problem.

### Missing or Corrupted Data

**Issue**: Data files needed for detection or training are missing.

**Solution**:
- Verify that the repository was cloned correctly.
- Check if data directories exist and have proper permissions.
- If data files were expected to be generated, ensure the generation steps were completed.
- Re-run the setup script to recreate necessary directories.

## Performance Issues

### Slow Detection

**Issue**: Detection algorithms take too long to run.

**Solution**:
- Consider using a more efficient algorithm (e.g., Random Forest instead of SVM for large datasets).
- Reduce the amount of data being processed if possible.
- Check if your system meets the minimum hardware requirements.
- Close other resource-intensive applications while running the detection.

### High CPU/Memory Usage

**Issue**: The application uses excessive system resources.

**Solution**:
- Use lighter-weight algorithms when possible.
- Process smaller batches of data at a time.
- Increase system memory if possible.
- Enable swap space on systems with limited RAM.

## Customization and Advanced Issues

### Adding Custom Algorithms

**Issue**: Need to integrate a custom detection algorithm.

**Solution**:
- Place your algorithm implementation in the `DDoS-Attack-Detection-and-Mitigation/Codes/ml/` directory.
- Follow the existing code structure and class interfaces.
- Update the UI code to include your algorithm in the selection options.

### Integration with Existing Networks

**Issue**: Configuring the system for a specific network setup.

**Solution**:
- Modify the network interface settings in the configuration files.
- Adapt the data collection modules to your specific network topology.
- Consider using passive monitoring mode for initial testing.

## Getting Further Help

If you encounter issues not covered in this guide:

1. Check the [GitHub repository issues](https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation/issues) for similar problems and solutions.
2. Submit a new issue on the GitHub repository with detailed information about your problem.
3. Include error messages, your system configuration, and steps to reproduce the issue.

## Common Error Messages and Solutions

### "ImportError: No module named 'X'"

**Solution**: Install the missing Python module: `python3 -m pip install X`

### "Permission denied"

**Solution**: 
- Ensure scripts are executable: `chmod +x install.sh run.sh`
- Run scripts with appropriate permissions (use sudo if necessary).

### "Address already in use"

**Solution**: 
- Find and stop the process using port 5000: `sudo lsof -i :5000` then `kill -9 PID`
- Change the port in run.sh or main.py if needed.

### "RuntimeError: Model not found"

**Solution**:
- Ensure models directory exists and has correct permissions.
- Run the appropriate model training scripts.
- Check file paths in the code.

## Security Considerations

- The system is designed for educational and defensive purposes only.
- Be cautious when running traffic generation scripts, as they could impact network performance.
- Always get proper authorization before deploying on production networks.
- Use responsible disclosure if you discover security vulnerabilities in the system.