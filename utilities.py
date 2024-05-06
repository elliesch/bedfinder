#Utilities.py

import pandas as pd

def inputs_to_pandas(input_csv):
        
    csv = pd.read_csv(input_csv)
    X = csv[['Topo', 'Bed', 'Elong', 'Area']] #input data that will be used to train the results
    
    X['Topo'][X['Topo'] == 'O']=1
    X['Topo'][X['Topo'] == 'V']=0
    X['Bed'][X['Bed'] == 'C']=1
    X['Bed'][X['Bed'] == 'S']=0
    
    #X = X.astype('int8') #change all columns of the input dataset to integers from string
    #add preprocess codes to one hot encode
    
    return X


