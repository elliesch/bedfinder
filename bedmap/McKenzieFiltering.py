''' McKenzie et al., 2022 Filtering -- Post Data-Collection Down Sampling Functionality '''

import joblib
import pandas as pd
from utilities import inputs_to_pandas
import warnings
warnings.filterwarnings('ignore')
     
csv = inputs_to_pandas('~/rf_bedform_mapping/data/BedformData.csv')
#need to edit all BedformData.csv to include site # so that these data may be filtered

#Downsample to n using scientific decisions
#Chautauqua New York US
site_1_mask = ((csv['site'] == 1) & 
               (csv['Area'] > 20000 & csv['Area'] < 400000) &
               (csv['MBG_Orient'] > 120 & csv['MBG_Orient'] < 180))

#Bardardalur Iceland
site_2_mask = ((csv['site'] == 2) & 
               (csv['MBG_Length'] > 300 & csv['MBG_Width'] > 150 & csv['MBG_Width'] < 900) &
               (csv['MBG_Orient'] > 0 & csv['MBG_Orient'] < 180))

#M'Clintock Channel Canada
site_3_mask = ((csv['site'] == 3) & 
               (csv['MBG_Length'] > 2.5 & csv['MBG_Length'] < 7400 & csv['MBG_Width'] < 1075) &
               (csv['MBG_Orient'] > 0 & csv['MBG_Orient'] < 180) &
               (csv['Area'] > 410000)) 

#Northern Norway
site_4_mask = ((csv['site'] == 4) & 
               (csv['MBG_Length']/['MBG_Width'] > 3) &
               (csv['MBG_Orient'] > 30 & csv['MBG_Orient'] < 330) &
               (csv['Area'] > 50000 & csv['Area'] < 450000)) 

#Nunavut Canada
site_5_mask = ((csv['site'] == 5) & 
               (csv['MBG_Length']/['MBG_Width'] > 3) &
               (csv['MBG_Orient'] > 100 & csv['MBG_Orient'] < 180) &
               (csv['Area'] > 7000)) 

#Northwestern Pennsylvania US
site_6_mask = ((csv['site'] == 6) & 
               (csv['MBG_Orient'] > 90 & csv['MBG_Orient'] < 180) &
               (csv['Area'] > 20000 & csv['Area'] < 900000))     

#Prince Wales Island Canada
site_7_mask = ((csv['site'] == 7) & 
               (csv['MBG_Length'] > 300 & csv['MBG_Width'] < 900) &
               (csv['MBG_Orient'] > 160 & csv['MBG_Orient'] < 180))     

#Puget Lowland Washington US
site_8_mask = ((csv['site'] == 8) & 
               (csv['MBG_Length'] > 660 & csv['MBG_Width'] > 200 & csv['MBG_Width'] < 1020) &
               (csv['MBG_Orient'] > 15 & csv['MBG_Orient'] < 50))    

#Northern Sweden
site_9_mask = ((csv['site'] == 9) & 
               (csv['MBG_Length'] > 440 & csv['MBG_Length'] < 3850) &
               (csv['MBG_Width'] > 85 & csv['MBG_Width'] < 1065) &
               (csv['MBG_Orient'] > 45 & csv['MBG_Orient'] < 95) & 
               (csv['Area'] > 65000) &
               (csv['MBG_Length']/csv['MBG_Width'] > 5))      

#create downsampled dataset using site masks:
csv_filtered = csv.loc[site_1_mask | site_2_mask | site_3_mask | site_4_mask | site_5_mask | site_6_mask | site_7_mask | site_8_mask | site_9_mask]

    
 