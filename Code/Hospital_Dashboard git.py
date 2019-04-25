 # -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:58:16 2019

@author: B McDaniel
"""

import pandas as pd

psi_data = pd.read_csv('c:/Users/Bonnie/Documents/GitHub/Hospital-Dashboard/Data_Clean/psi_data.csv', dtype ={'Zip_Code':'str'},index_col=0)
psi_data_df.index.astype(str,copy=False)
#psi_data.info()

zipcode_list = psi_data_df['Zip_Code'].tolist()
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

confirm = input("Is the hospital listed correct? Enter 'Y' or 'N':  ")

if confirm = 'Y':
    #create input for plot from selection
else:
    hospital_zip = get_zip()





#connect to local host to display and format








        



