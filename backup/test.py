# None = 2, Norm = 0,

set(df['max_glu_serum'])
{'>300', 'None', 'Norm', '>200'} # 1,2,0,3

set(df['A1Cresult'])
{'>8', 'None', 'Norm', '>7'}# 1,2,0,3

set(df['change'])
{'Ch', 'No'} #1,0

set(df['diabetesMed'])
{'Yes', 'No'} #1,0

set(df['readmitted'])
{'<30', '>30', 'NO'} # 1,3,0

set(df['metformin'])
{'Up', 'Down', 'Steady', 'No'} # 1,0,3,2

for i in attributes:
   print(set(df[i]), i)

# {0, 1, 2, 3} metformin
# {0, 1, 2, 3} repaglinide
# {0, 1, 2, 3} nateglinide
# {0, 1, 2, 3} chlorpropamide
# {0, 1, 2, 3} glimepiride
# {2, 3} acetohexamide
# {0, 1, 2, 3} glipizide
# {0, 1, 2, 3} glyburide
# {2, 3} tolbutamide
# {0, 1, 2, 3} pioglitazone
# {0, 1, 2, 3} rosiglitazone
# {0, 1, 2, 3} acarbose
# {0, 1, 2, 3} miglitol
# {2, 3} troglitazone
# {1, 2, 3} tolazamide
# {2} examide
# {2} citoglipton
# {0, 1, 2, 3} insulin
# {0, 1, 2, 3} glyburide-metformin
# {2, 3} glipizide-metformin
# {2, 3} glimepiride-pioglitazone
# {2, 3} metformin-rosiglitazone
# {2, 3} metformin-pioglitazone

age = {'[40-50)', '[60-70)', '[90-100)', '[70-80)', '[20-30)', '[0-10)', '[50-60)', '[10-20)', '[80-90)', '[30-40)'}

for a in age:
    no = a[1:3].strip("-")
    print(int(no) +5)


for i in attributes:
    print(len(df) - len(df[i][df[i] == 2]), i)

# 19988 metformin
# 1539 repaglinide
# 703 nateglinide
# 86 chlorpropamide
# 5191 glimepiride
# 1 acetohexamide
# 12686 glipizide
# 10650 glyburide
# 23 tolbutamide
# 7328 pioglitazone
# 6365 rosiglitazone
# 308 acarbose
# 38 miglitol
# 3 troglitazone
# 39 tolazamide
# 0 examide
# 0 citoglipton
# 54383 insulin
# 706 glyburide-metformin
# 13 glipizide-metformin
# 1 glimepiride-pioglitazone
# 2 metformin-rosiglitazone
# 1 metformin-pioglitazone

# df.isnull().sum()
# Pregnancies                 0
# Glucose                     0
# BloodPressure               0
# SkinThickness               0
# Insulin                     0
# BMI                         0
# DiabetesPedigreeFunction    0
# Age                         0
# Outcome                     0
# dtype: int64

set(df['race'])
{'?', 'AfricanAmerican', 'Asian', 'Other', 'Caucasian', 'Hispanic'}