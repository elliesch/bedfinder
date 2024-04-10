''' Bed Mapping Script -- Core Functionality '''

import joblib
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
import warnings
warnings.filterwarnings('ignore')


class ClassifyBedforms:
    '''
    write a docstring here
    '''
    
    def __init__(self, input_csv):
        
        self.X_test = self.inputs_to_pandas(input_csv)
        self.predicted_bedform, self.bedform_probability = self.classify_bedforms(self.X_test)
        
    def classify_bedforms(self, X_test):
        
        rf_model = joblib.load('RandomForest.pkl')
        
        y_est = rf_model.predict(X_test)
        y_est_prob = rf_model.predict_proba(X_test)
        
        return y_est, y_est_prob

    def inputs_to_pandas(self, input_csv):
        
        csv = pd.read_csv(input_csv)
        X = csv[['Topo', 'Bed', 'Elong', 'Area']] #input data that will be used to train the results

        X['Topo'][X['Topo'] == 'O']=1
        X['Topo'][X['Topo'] == 'V']=0
        X['Bed'][X['Bed'] == 'C']=1
        X['Bed'][X['Bed'] == 'S']=0

        X = X.astype('int8') #change all columns of the input dataset to integers from string
        #add preprocess codes to one hot encode
        
        return X
