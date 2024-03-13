''' Bed Mapping Script -- Core Functionality '''

import joblib
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold


class ClassifyBedforms:
    
    def __init__(self, input_csv):
        
        self.X_test = self.inputs_to_pandas(input_csv)
        self.bedform = self.classify_bedforms(self.X_test)
        
    def classify_bedforms(self, X_test):
        
        rf_model = joblib.load('RandomForest.pkl')
        
        y_est = rf_model.predict(X_test)
        
        return y_est

    def inputs_to_pandas(self, input_csv):
        
        #add import csv
        
        #add preprocess codes to one hot encode
        
        return X
