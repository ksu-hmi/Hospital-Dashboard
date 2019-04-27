# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 00:21:57 2019

@author: Bonnie McDaniel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

psi_data_df = pd.read_csv('c:/data/TEST/psi_data.csv', dtype = {'Zip_Code':'str'})
psi_data_df.index.astype(str, copy=False)
#psi_data_df.info()
zipcode_list = psi_data_df["Zip_Code"].tolist()


def get_zip():
    match = 0
    while match == 0:
        choose_zip=input("Please enter the zip code for the hospital you want to view or q to quit: ").lower()
        if choose_zip in zipcode_list:
           match = match + 1
           if choose_zip == "q":
               print("Thank you for visiting this site")
        else: 
            print("Zip code not found, please try again")

    return choose_zip

hospital_zip = get_zip()

print(psi_data_df.loc[psi_data_df['Zip_Code']== hospital_zip,['Provider_ID','Provider_Name']])

confirm = input("Is this the correct hospital? Enter 'Y' or 'N': ").upper()

if confirm == "Y":
    results_df = psi_data_df.loc[psi_data_df['Zip_Code']== hospital_zip,['Provider_ID','Provider_Name','City','State','Zip_Code','PSI-10','PSI-11','PSI-12','PSI-13','PSI-14','PSI-15','PSI-3','PSI-6','PSI-8','PSI-9','PSI-90']]
    print(results_df)
else:
    hospital_zip = get_zip()    


#https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/


#https://thispointer.com/select-rows-columns-by-name-or-index-in-dataframe-using-loc-iloc-python-pandas/

