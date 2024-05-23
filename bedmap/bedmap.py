''' Bed Mapping Script -- Core Functionality '''

import pandas as pd
import numpy as np
import warnings
from .utilities import thresh, load_model
warnings.filterwarnings('ignore')


class ClassifyBedforms:
    '''
    Classify bedforms based on input features using machine learning models.

    Parameters:
    -----------
    input_csv : str
        Path to the input CSV file containing features for classification.
    model : {'ensemble_average', 'random_forest', 'xgboost'}, default='ensemble_average'
        The classification model to be used.
    threshold : float, default=0.45
        Threshold for classifying bedforms based on predicted probabilities.
    probability : bool, default=False
        If True, returns the predicted probabilities; if False, returns binary predictions.

    Attributes:
    -----------
    X_test : pandas.DataFrame
        Features extracted from the input CSV file for classification.
    predicted_bedforms : numpy.ndarray
        Predicted bedforms based on the chosen model and settings.

    Methods:
    --------
    classify_bedforms(X_test, model, threshold, probability)
        Classifies bedforms based on input features using the specified model.
    inputs_to_pandas(input_csv)
        Reads input CSV file and processes features for classification.
    '''
    
    def __init__(self, input_csv, 
                 model='ensemble_average',
                 threshold=0.45,
                 probability=False
                ):
        
        self.X_test = self.inputs_to_pandas(input_csv)
        self.predicted_bedforms = self.classify_bedforms(self.X_test, model=model,
                                                         threshold=threshold,
                                                         probability=probability)

    
    def classify_bedforms(self, X_test, model, threshold, probability):

        if model not in ['random_forest', 'xgboost', 'ensemble_average']:
            raise ValueError("Invalid model choice. Allowed values are 'random_forest', 'xgboost', or 'ensemble_average'.")

        if model == 'random_forest':

            #Load and predict bedforms using Random Forest
            rf_model=load_model('bedmap.models', 'RandomForest.pkl')
            y_est_prob = rf_model.predict_proba(X_test)

            #Return thresholded predictions
            if probability == False:
                y_est = thresh(y_est_prob[:,1], threshold)
                
                return y_est

            #Return probabilities
            else:
                return y_est_prob[:,1]

        if model == 'xgboost':

            #Load and predict bedforms using XGBoost
            xgb_model=load_model('bedmap.models', 'XGBoost.pkl')
            y_est_prob = xgb_model.predict_proba(X_test)

            #Return thresholded predictions
            if probability == False:
                y_est = thresh(y_est_prob[:,1], threshold)
                
                return y_est
                
            #Return probabilities
            else:
                return y_est_prob[:,1]

        if model == 'ensemble_average':

            #Calculate Ensemble Average of RF and XGB predictions
            rf_model=load_model('bedmap.models', 'RandomForest.pkl')
            xgb_model=load_model('bedmap.models', 'XGBoost.pkl')

            y_est_prob = np.mean([xgb_model.predict_proba(X_test), 
                                  rf_model.predict_proba(X_test)], 
                                  axis=0)
            
            #Return thresholded predictions            
            if probability == False:
                y_est = thresh(y_est_prob[:,1], threshold)
                
                return y_est

            #Return probabilities
            else:
                return y_est_prob[:,1]
        

    def inputs_to_pandas(self, input_csv):

        #Read in the csv file
        csv = pd.read_csv(input_csv)
        X = csv[['Topo', 'Bed', 'Elong', 'Area']] 

        #Binarize the Topo and Bed columns
        X['Topo'][X['Topo'] == 'O']=1
        X['Topo'][X['Topo'] == 'V']=0
        X['Bed'][X['Bed'] == 'C']=1
        X['Bed'][X['Bed'] == 'S']=0

        #Convert Topo and Bed columns to integers
        X['Topo'] = X['Topo'].astype('int')
        X['Bed'] = X['Bed'].astype('int')

        #One-hot-encode Topo and Bed columns
        X.rename(columns={'Bed': 'Bed_C'}, inplace=True)
        X.rename(columns={'Topo': 'Topo_O'}, inplace=True)
        X['Topo_V'] = (X['Topo_O'] == 0).astype(int)
        X['Bed_S'] = (X['Bed_C'] == 0).astype(int)
        
        return X