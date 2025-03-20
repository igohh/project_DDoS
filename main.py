import os
import sys
import logging
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
import subprocess
from datetime import datetime
import json

# Setup basic logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Add project directory to path
repo_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DDoS-Attack-Detection-and-Mitigation')
sys.path.append(repo_dir)
sys.path.append(os.path.join(repo_dir, 'Codes'))
sys.path.append(os.path.join(repo_dir, 'Codes/ml'))

# Import ML modules
try:
    from Codes.ml.ML import MachineLearning
    logger.info("Successfully imported ML modules")
except Exception as e:
    logger.error(f"Error importing ML modules: {e}")

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "ddos_detection_secret_key")
app.config['UPLOAD_FOLDER'] = os.path.join(repo_dir, 'results')
app.config['MODELS_FOLDER'] = os.path.join(repo_dir, 'models')

# Ensure the upload and models folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['MODELS_FOLDER'], exist_ok=True)

# Helper function to create plots
def create_plot(data, plot_type='bar', title='Data Visualization'):
    plt.figure(figsize=(10, 6))
    if plot_type == 'bar':
        sns.barplot(data=data)
    elif plot_type == 'line':
        sns.lineplot(data=data)
    elif plot_type == 'heatmap':
        sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    
    plt.title(title)
    plt.tight_layout()
    
    # Save plot to a base64 string
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    plt.close()
    return base64.b64encode(image_png).decode('utf-8')

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # Sample visualization (would be replaced with actual data)
    sample_data = pd.DataFrame({
        'Normal Traffic': [95, 105, 90, 110, 120],
        'DDoS Traffic': [5, 10, 15, 20, 25]
    }, index=['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'])
    
    bar_plot = create_plot(sample_data, plot_type='bar', title='Traffic Comparison')
    line_plot = create_plot(sample_data, plot_type='line', title='Traffic Trends')
    
    # Example results - these would come from actual detection
    detection_results = {
        'total_packets': 1000,
        'normal_packets': 900,
        'ddos_packets': 100,
        'detection_rate': 90.0,
        'false_positive_rate': 2.5
    }
    
    return render_template('dashboard.html', 
                          bar_plot=bar_plot, 
                          line_plot=line_plot,
                          results=detection_results)

@app.route('/detection')
def detection():
    # Keeping only the 4 highest-accuracy ML models: RF, SVM, DT, KNN
    ml_algorithms = ['KNN', 'SVM', 'DT', 'RF']
    return render_template('detection.html', ml_algorithms=ml_algorithms)

@app.route('/run_detection', methods=['POST'])
def run_detection():
    try:
        algorithm = request.form.get('algorithm')
        if not algorithm:
            flash('Please select an algorithm', 'danger')
            return redirect(url_for('detection'))
        
        logger.info(f"Running detection with algorithm: {algorithm}")
        
        # In a real implementation, this would call the actual ML code
        # For demonstration, we'll simulate a successful detection
        
        # Simulate results
        accuracy = np.random.uniform(75, 98)
        precision = np.random.uniform(70, 95)
        recall = np.random.uniform(70, 95)
        f1_score = np.random.uniform(70, 95)
        
        # Create a timestamp for this run
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save results to a JSON file
        results = {
            'algorithm': algorithm,
            'timestamp': timestamp,
            'metrics': {
                'accuracy': float(accuracy),
                'precision': float(precision),
                'recall': float(recall),
                'f1_score': float(f1_score)
            }
        }
        
        results_file = os.path.join(app.config['UPLOAD_FOLDER'], f'detection_results_{timestamp}.json')
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=4)
        
        logger.info(f"Results saved to: {results_file}")
        
        # Store results in session for display
        session['detection_results'] = results
        
        flash(f'Detection completed successfully using {algorithm}', 'success')
        return redirect(url_for('results'))
    
    except Exception as e:
        logger.error(f"Error running detection: {e}")
        flash(f'Error running detection: {str(e)}', 'danger')
        return redirect(url_for('detection'))

@app.route('/results')
def results():
    detection_results = session.get('detection_results')
    
    if not detection_results:
        # Check if there are any result files
        result_files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) 
                       if f.startswith('detection_results_') and f.endswith('.json')]
        
        if result_files:
            # Load the latest result file
            latest_file = sorted(result_files)[-1]
            with open(os.path.join(app.config['UPLOAD_FOLDER'], latest_file), 'r') as f:
                detection_results = json.load(f)
        else:
            flash('No detection results found. Please run a detection first.', 'info')
            return redirect(url_for('detection'))
    
    # Create confusion matrix visualization (simulated for demonstration)
    confusion_matrix = np.array([
        [int(detection_results['metrics']['accuracy'] * 2), 
         int((100 - detection_results['metrics']['precision']) / 2)],
        [int((100 - detection_results['metrics']['recall']) / 2), 
         int(detection_results['metrics']['f1_score'] * 2)]
    ])
    
    confusion_df = pd.DataFrame(
        confusion_matrix,
        index=['Actual Normal', 'Actual DDoS'],
        columns=['Predicted Normal', 'Predicted DDoS']
    )
    
    confusion_plot = create_plot(confusion_df, plot_type='heatmap', 
                               title=f"Confusion Matrix - {detection_results['algorithm']}")
    
    return render_template('results.html', 
                          results=detection_results,
                          confusion_plot=confusion_plot)

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

# Mitigation module removed as requested

@app.route('/about')
def about():
    return render_template('about.html')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)