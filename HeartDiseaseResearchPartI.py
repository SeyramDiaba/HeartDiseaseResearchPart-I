# import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import binom_test

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

# Assign hd chol values as chol_hd variable
chol_hd= yes_hd['chol']



# Mean cholesterol value of patients diagnosed with hd
print('Mean value of patients with HD ',chol_hd.mean())

# Hypothesis test 
sig_thresh = 0.05
tstat, pval = ttest_1samp(chol_hd, 240)
print('pval is',pval/2) # this is way below the significane threshold making the null hypothesis false

# Assigning cholesterol values of patients with no heart disease to 'chol_nhd'
chol_nhd = no_hd['chol']
print(chol_nhd.head())

# Mean cholesterol value of patients with no heart disease
print('Mean value of patients without HD ',chol_nhd.mean())

# Hypothesis Test for NHD
tstat, pval = ttest_1samp(chol_nhd, 240)
print('pval nhd is',pval/2)

# total number of patients in dataset 'heart'
num_patients = len(heart)
print('Total number of patients:', num_patients)

# total number of patients with fasting blood sugar greater then 120
num_highfbs_patients = heart[heart['fbs']==1]
print('Number of Patients with fbs greater than 120:', len(num_highfbs_patients))

# 8% of the sample test
print(num_patients *0.08)

# binomial test
pval = binom_test(len(num_highfbs_patients),num_patients, 0.08, alternative = 'greater')
print(pval)