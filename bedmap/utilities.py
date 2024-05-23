#Utilities.py

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_rate_matrix(conf_matrix, title='Confusion Matrix'):
    '''
    Takes in sklearn's confusion_matrix object and 
    plots a True Positive Rate matrix
    '''

    
    # Calculate True Negative Rate (TNR), False Positive Rate (FPR),
    # False Negative Rate (FNR), and True Positive Rate (TPR)
    tn = conf_matrix[0, 0]
    fp = conf_matrix[0, 1]
    fn = conf_matrix[1, 0]
    tp = conf_matrix[1, 1]
    
    tnr = tn / (tn + fp)
    fpr = fp / (tn + fp)
    fnr = fn / (tp + fn)
    tpr = tp / (tp + fn)
    
    rate_matrix = np.array([[tnr, fpr],
                            [fnr, tpr]])
    
    # Plot confusion matrix
    plt.imshow(rate_matrix, interpolation='nearest', cmap=plt.cm.Blues, vmin=0, vmax=1)
    plt.title(title)
    
    # Add colorbar
    plt.colorbar()
    
    # Add labels
    classes = ['Negative', 'Positive'] 
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    
    # Add text annotations
    thresh = rate_matrix.max() / 2.
    for i in range(rate_matrix.shape[0]):
        for j in range(rate_matrix.shape[1]):
            plt.text(j, i, format(rate_matrix[i, j], '.2f'),
                     horizontalalignment="center",
                     color="white" if rate_matrix[i, j] > thresh else "black")
    
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()
    plt.show()

def thresh(array, threshold):
    '''
    Binarizes an array of probability thresholds
    to chosen threshold
    '''
    mod_array = (array >= threshold).astype(int)
    
    return mod_array
