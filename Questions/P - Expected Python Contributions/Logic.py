import pandas as pd
def preprocess_data(df):
    """
    This function returns all repos with python as primary language, the pushed data of the repo, 
    and the number of pull requests for the repo.
    """
    df = df.copy()
    df = df[df['primaryLanguage'] == 'Python']
    df = df[['primaryLanguage', 'pushedAt', 'pullRequests']]
    df['pushedAt'] = pd.to_datetime(df['pushedAt'])
    df['year'] = df['pushedAt'].dt.year
    df['year'] = df['year'].astype('int64')
    df.drop('pushedAt', axis = 1, inplace = True)
    df = df[df['year'] != 2023]
    return df

def explore_data(df):
    print("Number of repos with python as primary language: ", df.shape[0])
    print("Available years from {} to {}".format(df['year'].min(), df['year'].max()))
    print("Number of pull requests over all python repos from 2009 to 2022: ", df['pullRequests'].sum())

    for year in range(df['year'].min(), df['year'].max() + 1):
        print("Number of pull requests in {}: {}".format(year, df[df['year'] == year]['pullRequests'].sum()))
