 # -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:58:16 2019

@author: B McDaniel
"""

import pandas as pd

psi_data = pd.read_csv('c:/Users/Bonnie/Documents/GitHub/Hospital-Dashboard/Data_Clean/psi_data.csv', dtype ={'Zip_Code':'str'},index_col=0)
psi_data.info()

zipcode_list = list(df_psi_data.Zip_Code)
hospital_list=[]

choose_zip=input("Please enter the zip code for the hospital you want to view: ")

for zip in zipcode_list:
    if choose_zip in zipcode_list:
        print(df_psi_data.Provider_ID,df_psi_data.Provider_Name)
    else:
        print("Zip code not found")

        



