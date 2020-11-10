import pandas as pd
from getFlightsFromApi import *
pd.options.display.max_columns= None

def getHotelsFromDataSet(country):
    df = pd.read_csv("Hotel_Reviews.csv")
    deleteColumnFromDataType(['Hotel_Address','Review_Date','Average_Score', 'Review_Total_Negative_Word_Counts','Review_Total_Negative_Word_Counts','Additional_Number_of_Scoring', 'Negative_Review','Positive_Review',
       'Review_Total_Positive_Word_Counts', 'Total_Number_of_Reviews_Reviewer_Has_Given', 'Tags', 'days_since_review',
          'lat','lng'], df)
    df['Reviewer_Nationality'] = df['Reviewer_Nationality'].str.strip()
    sortValues(df, 'Reviewer_Score', False)
    df = df[df['Reviewer_Nationality'] == country]
    return df.head()




