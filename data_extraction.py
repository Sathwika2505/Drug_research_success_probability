import pandas as pd

def data_extraction():
    df = pd.read_csv("cardiozen_manufacturing_data.csv")
    print(df)
    
    return df
    
data_extraction()