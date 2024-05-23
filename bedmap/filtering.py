''' McKenzie et al., 2022 Filtering -- Post Data-Collection Down Sampling Functionality '''

import joblib
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

class McKenzieFiltering:
    '''Scientifically-driven filtering decision making.
   
    Parameters:
    -----------
    data_path : str
        Path to the input CSV file containing features for classification.
    
    Attributes:
    -----------
    csv : pandas.DataFrame
        Features from the input CSV file that will be run through filtering.
    csv_filtered : pandas.DataFrame
        Filtered bedforms based on the chosen filter settings for feature length, width, elongation, area, and orientation.

    Methods:
    --------
    mckenzie_filtering(self, csv)
        Filters bedforms based on input parameters using the specified filters for each site.
    '''

    def __init__(self, data_path):
        self.csv = pd.read_csv(data_path)
        self.csv_filtered = self.mckenzie_filtering(self.csv)

    def mckenzie_filtering(self, csv):
            
        #Downsample to n using scientific decisions
        #Chautauqua New York US
        Site_1_mask = ((csv['Site'] == 1) & 
                       ((csv['Area'] > 20000) & (csv['Area'] < 400000)) &
                       ((csv['Orient'] > 120) & (csv['Orient'] < 180)))
        
        #Bardardalur Iceland
        Site_2_mask = ((csv['Site'] == 2) & 
                       ((csv['Length'] > 300) & (csv['Width'] > 150) & (csv['Width'] < 900)) &
                       ((csv['Orient'] > 0) & (csv['Orient'] < 180)))
        
        #M'Clintock Channel Canada
        Site_3_mask = ((csv['Site'] == 3) & 
                       ((csv['Length'] > 2.5) & (csv['Length'] < 7400) & (csv['Width'] < 1075)) &
                       ((csv['Orient'] > 0) & (csv['Orient'] < 181)) &
                       (csv['Area'] < 410000)) 
        
        #Northern Norway
        Site_4_mask = ((csv['Site'] == 4) & 
                       (csv['Elong'] > 3) &
                       ((csv['Orient'] > 30) & (csv['Orient'] < 330)) &
                       ((csv['Area'] > 50000) & (csv['Area'] < 450000))) 
        
        #Nunavut Canada
        Site_5_mask = ((csv['Site'] == 5) & 
                       (csv['Elong'] > 3) &
                       ((csv['Orient'] > 100) & (csv['Orient'] < 180)) &
                       (csv['Area'] > 7000)) 
        
        #Northwestern Pennsylvania US
        Site_6_mask = ((csv['Site'] == 6) & 
                       ((csv['Orient'] > 90) & (csv['Orient'] < 180)) &
                       ((csv['Area'] > 20000) & (csv['Area'] < 900000)))     
        
        #Prince Wales Island Canada
        Site_7_mask = ((csv['Site'] == 7) & 
                       ((csv['Length'] > 300) & (csv['Width'] < 900)) &
                       ((csv['Orient'] > 160) & (csv['Orient'] < 180)) |
                        ((csv['Orient'] > 315) & (csv['Orient'] < 40)))     
        
        #Puget Lowland Washington US
        Site_8_mask = ((csv['Site'] == 8) & 
                       ((csv['Length'] > 660) & (csv['Width'] > 200) & (csv['Width'] < 1020)) &
                       ((csv['Orient'] > 15) & (csv['Orient'] < 50)))    
        
        #Northern Sweden
        Site_9_mask = ((csv['Site'] == 9) & 
                       ((csv['Length'] > 440) & (csv['Length'] < 3850)) &
                       ((csv['Width'] > 85) & (csv['Width'] < 1065)) &
                       ((csv['Orient'] > 45) & (csv['Orient'] < 95)) |
                       ((csv['Orient'] > 225) & (csv['Orient'] < 270)) & 
                       (csv['Area'] > 65000) &
                       (csv['Elong'] > 5))       

        #create downsampled dataset using site masks:
        csv_filtered = csv.loc[Site_1_mask | Site_2_mask | Site_3_mask | Site_4_mask | Site_5_mask | Site_6_mask | Site_7_mask | Site_8_mask | Site_9_mask]
            
        return csv_filtered

