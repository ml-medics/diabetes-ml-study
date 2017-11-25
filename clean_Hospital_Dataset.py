import pandas as pd
import numpy as np
from BDA.Diabetes_project import classification
df = pd.read_csv("E:/1RIT/BDA/project/dataset/diabetic_data.csv")

'''
    Removing unwanted and attributes containing more than 50% missing values
'''
bad_features = ['encounter_id', 'patient_nbr','weight', 'payer_code',
                'admission_type_id','discharge_disposition_id',
                'admission_source_id','medical_specialty', 'num_lab_procedures', 'num_procedures',
               'num_medications', 'number_outpatient', 'number_emergency',
               'number_inpatient', 'diag_1', 'diag_2', 'diag_3',
               'number_diagnoses','examide','citoglipton']

df.drop(bad_features, inplace=True, axis =1)

#converting nominal or categorical data to numerical data.

df.loc[df['diabetesMed'] == "Yes", 'diabetesMed'] = 1
df.loc[df['diabetesMed'] == "No", 'diabetesMed'] = 0
df.loc[df['change'] == "ch",'diabetesMed'] = 1
df.loc[df['chen'] == "ch",'diabetesMed'] = 1

df['diabetesMed'] = np.where(df['diabetesMed']=="Yes", 1,0)
df['change'] = np.where(df['change']=="Ch", 1,0)

attributes = [ 'metformin',
       'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride',
       'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide',
       'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol',
       'troglitazone', 'tolazamide', 'insulin',
       'glyburide-metformin', 'glipizide-metformin',
       'glimepiride-pioglitazone', 'metformin-rosiglitazone',
       'metformin-pioglitazone']
for i in attributes:
    df.loc[df[i] == "Up", i] = 1
    df.loc[df[i] == "Down", i] = 0
    df.loc[df[i] == "Steady", i] = 3
    df.loc[df[i] == "No", i] = 2

df.loc[df['max_glu_serum'] == ">300", 'max_glu_serum'] = 1
df.loc[df['max_glu_serum'] == ">200", 'max_glu_serum'] = 3
df.loc[df['max_glu_serum'] == "None", 'max_glu_serum'] = 2
df.loc[df['max_glu_serum'] == "Norm", 'max_glu_serum'] = 0

df.loc[df['A1Cresult'] == ">8", 'A1Cresult'] = 1
df.loc[df['A1Cresult'] == ">7", 'A1Cresult'] = 3
df.loc[df['A1Cresult'] == "None", 'A1Cresult'] = 2
df.loc[df['A1Cresult'] == "Norm", 'A1Cresult'] = 0

df.loc[df['readmitted'] == "<30", 'readmitted'] = 1
df.loc[df['readmitted'] == ">30", 'readmitted'] = 3
df.loc[df['readmitted'] == "NO", 'readmitted'] = 0

df.loc[df['gender'] == "Male", 'gender'] = 1
df.loc[df['gender'] == "Female", 'gender'] = 2
df.loc[df['gender'] == "Unknown/Invalid", 'gender'] = 3

age = {'[40-50)', '[60-70)', '[90-100)', '[70-80)', '[20-30)', '[0-10)', '[50-60)', '[10-20)', '[80-90)', '[30-40)'}

for a in age:
    no = a[1:3].strip("-")
    df.loc[df['age'] == a, 'age'] = int(no)+5

skewedEntries = []
for i in attributes:
    if (len(df) - len(df[i][df[i] == 2])) < 10:
        skewedEntries.append(i)
df.drop(skewedEntries, inplace = True, axis =1)

race_dict = {'?':5, 'AfricanAmerican':1, 'Asian':4, 'Other':5, 'Caucasian':3, 'Hispanic':2}

df.loc[df['race'] =="AfricanAmerican", 'race'] = race_dict.get("AfricanAmerican")
df.loc[df['race'] =="Asian", 'race'] = race_dict.get("Asian")
df.loc[df['race'] =="Caucasian", 'race'] = race_dict.get("Caucasian")
df.loc[df['race'] =="Hispanic", 'race'] = race_dict.get("Hispanic")
df.loc[df['race'] =="?", 'race'] = race_dict.get("Other")
df.loc[df['race'] =="Other", 'race'] = race_dict.get("Other")

df.to_csv('diabetic_data_clean.csv')
#df = pd.read_csv('diabetic_data_clean.csv')
pima = pd.read_csv('dataset/diabetes.csv')
cl = classification.classification(pima, "PIMA")
classification.classification(df, "HOSPITAL_DATASET")
