from data_analysis import data_analysis

def feature_engineering():
    data = data_analysis()
    data.to_csv('drug_research_success_probability.csv', index=False)

    print(data.dtypes)

    return data

feature_engineering()