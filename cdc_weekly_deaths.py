import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
import seaborn as sns

# https://data.cdc.gov/NCHS/Weekly-Counts-of-Deaths-by-State-and-Select-Causes/muzy-jte6
df = pd.read_csv(r'C:\Users\steve\Downloads\wkly_dths_2.csv') 
df = df[df['Jurisdiction of Occurrence'] == 'United States']
df_causes_wkly = df[[
        'Week Ending Date', 
        'Septicemia (A40-A41)',
        'Malignant neoplasms (C00-C97)',
        'Diabetes mellitus (E10-E14)', 'Alzheimer disease (G30)',
        'Influenza and pneumonia (J09-J18)',
        'Chronic lower respiratory diseases (J40-J47)',
        'Other diseases of respiratory system (J00-J06,J30-J39,J67,J70-J98)',
        'Nephritis, nephrotic syndrome and nephrosis (N00-N07,N17-N19,N25-N27)',
        'Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified (R00-R99)',
        'Diseases of heart (I00-I09,I11,I13,I20-I51)',
        'Cerebrovascular diseases (I60-I69)',
        'COVID-19 (U071, Multiple Cause of Death)',
        'COVID-19 (U071, Underlying Cause of Death)']]
    
    
# seaborn plotting
# NUM_COLORS = len(df_causes_wkly.drop('Week Ending Date',axis=1).columns)
colors = ['black', 'darkorange', 'limegreen', 'forestgreen', 'royalblue', 
            'lightsteelblue', 'blueviolet', 'thistle', 'magenta', 'crimson',
            'goldenrod', 'olive', 'lightsalmon'] # need to automate color selection with axes.set_prop_cycle
plt.stackplot(
    pd.to_datetime(df_causes_wkly['Week Ending Date']).values, 
    df_causes_wkly.drop('Week Ending Date',axis=1).replace(',','', regex=True).apply(pd.to_numeric).T,
    labels = df_causes_wkly.drop('Week Ending Date',axis=1).columns,
    colors = colors
    )
plt.xticks(rotation=70)
plt.gca().xaxis.set_major_locator(dates.AutoDateLocator())
plt.gca().xaxis.set_major_formatter(dates.DateFormatter("%m - %y"))
plt.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0)
plt.savefig("output.png", bbox_inches='tight')
plt.clf()
