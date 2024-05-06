#McKenzie filtering script
''' McKenzie et al., 2022 Filtering -- Post Data-Collection Functionality '''

import joblib
import pandas as pd
from utilities import inputs_to_pandas
import warnings
warnings.filterwarnings('ignore')
     
csv = inputs_to_pandas('~/rf_bedform_mapping/data/BedformData.csv')
#need to edit all BedformData.csv to include site # so that these data may be filtered

'''
Sample mask:
site_1_mask = ((csv['site'] == 1) & (csv['Area'] > 20000 & csv['Area'] < 400000) & (csv['MBG_Orient'] > 120 & csv['MBG_Orient'] < 180))

Sample pandas locater with masks:
csv_filtered = csv.loc[site_1_mask | site_2_mask]
'''

#Downsample to n using scientific decisions
for n in input_csv
    (for site == 1 #Chautauqua New York US
     if Area > 20000 and Area < 400000
     and MBG_Orient > 120 and MBG_Orient < 180)
    
    or
    
    (for site == 2 #Bardardalur Iceland
     if MBG_Length > 300
     and MBG_Width > 150 and MBG_Width < 900
     and MBG_Orient > 0 and MBG_Orient < 180)
    or

    for site == 3 #M'Clintock Channel Canada
    if MBG_Width < 1075
    and MBG_Length > 2.5 and MBG_Length < 7400
    and MBG_Orient > 0 and MBG_Orient < 180
    and Area > 4100000
    break
    
    for site == 4 #Northern Norway
    if Area > 50000 and Area < 450000
    and MBG_Length/MBG_Width > 5
    and MBG_Orient > 30 and MBG-Orient < 330
    break

    for site == 5 #Nunavut Canada
    if MBG_Orient > 100 and MBG_Orient < 180
    and MBG_Length/MBG_Width > 3
    and Area > 7000
    break

    for site == 6 #Northwestern Pennsylvania US
    if Area > 20000 and < 900000
    and MBG_Orient > 90 and MBG_Orient < 180
    break

    for site ==7 #Prince Wales Island Canada
    if MBG_Length > 300
    and MBG_Width < 900
    and MBG_Orient > 160 and MBG_Orient < 180
    break

    for site == 8 #Puget Lowland Washington US
    if MBG_Orient > 15 and MBG_Orient < 50
    and MBG_Length > 660
    and MBG_Width > 200 and MBG_Width < 1020
    break

    for site == 9 # Northern Sweden
    if Area > 65000
    and MBG_Length > 440 and MBG_Length < 3850
    and MBG_Width > 85 and MBG_Width < 1065
    and MBG_Orient > 45 and MBG_Orient < 95
    and MBG_Length/MBG_Width > 5
    break 
    
    x[n] 
    break 
    
 