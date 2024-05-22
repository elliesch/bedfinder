''' Bed Mapping Script for ArcGIS'''

### Check for missing packages and install them locally
import subprocess
import sys

def check_and_install_package(package_name):
    try:
        __import__(package_name)
        print(f"'{package_name}' is already installed.")
    except ImportError:
        print(f"'{package_name}' is not installed. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])


check_and_install_package('joblib')
check_and_install_package('pandas')
check_and_install_package('numpy')
check_and_install_package('scikit-learn')
check_and_install_package('xgboost')
check_and_install_package('bedmap')

### Import necessary packages
import pandas as pd
import numpy as np
import joblib
import sklearn
import xgboost
import warnings
warnings.filterwarnings('ignore')

### Import the data
newdata = pd.read_csv('update/path/here')

### Run bedmap with the Ensemble Average model at the recommended threshold
### NOTE THIS NEEDS TO BE UPDATED WITH NEW MODELS AND CORRECT CSV PATH ####
bedforms = ClassifyBedforms('update/path/here',
                            model='ensemble_average', 
                            threshold=0.45, probability=False)

predicted_bedforms = bedforms.predicted_bedforms

### Save the new data to a csv file
newdata['bedform_pred'] = predicted_bedforms.tolist()
newdata.to_csv('update/final/path/here', index=False)