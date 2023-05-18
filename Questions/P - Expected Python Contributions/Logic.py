import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
color_pal = sns.color_palette()
def preprocess_data(df):
    """
    This function returns all repos with python as primary language, the pushed data of the repo, 
    and the number of pull requests for the repo.
    """
    df = df.copy()
    df = df[df['primaryLanguage'] == 'Python']
    df = df[['primaryLanguage', 'pushedAt', 'pullRequests']]
    # df = df[['primaryLanguage', 'createdAt', 'pullRequests']]

    df['pushedAt'] = pd.to_datetime(df['pushedAt'])
    df['year'] = df['pushedAt'].dt.year
    df['month'] = df['pushedAt'].dt.month

    # df['createdAt'] = pd.to_datetime(df['createdAt'])
    # df['year'] = df['createdAt'].dt.year
    # df['month'] = df['createdAt'].dt.month


    df['year'] = df['year'].astype('int64')
    df['month'] = df['month'].astype('int64')
    # df['day'] = df['pushedAt'].dt.day
    # df['day'] = df['day'].astype('int64')
    # # print(df['day'].max())

    df.drop('pushedAt', axis = 1, inplace = True)
    # df.drop('createdAt', axis = 1, inplace = True)

    df = df[df['year'] != 2023]
    # df = df[df['year'] != 2022]
    # df = df[df['year'] != 2021]


    return df

def explore_data(df):
    print("Number of repos with python as primary language: ", df.shape[0])
    print("Available years from {} to {}".format(df['year'].min(), df['year'].max()))

    print("Number of pull requests over all python repos from 2009 to 2022: ", df['pullRequests'].sum())
    pullReqs = []
    date = []
    for year in range(df['year'].min(), df['year'].max() + 1):
        print("Number of pull requests in {}: {}".format(year, df[df['year'] == year]['pullRequests'].sum()))
        pullReqs.append(df[df['year'] == year]['pullRequests'].sum())
        date.append(str(year))
    pullReqsMonth = []
    dateMonth = []

    for year in range(df['year'].min(), df['year'].max() + 1):
        for month in range(1, 13):
            # print("Number of pull requests in {}-{}: {}".format(year, month, df[(df['year'] == year) & (df['month'] == month)]['pullRequests'].sum()))
            num = df[(df['year'] == year) & (df['month'] == month)]['pullRequests'].sum()
            if num != 0:
                pullReqsMonth.append(num)
                dateMonth.append(str(year) + '-' + str(month))
               


    draw_bar_plot(pullReqs, date)
    

    for i in range(1,20):
        print("Number of pull requests in {}-{}: {}".format(dateMonth[-i].split('-')[0], dateMonth[-i].split('-')[1], pullReqsMonth[-i]))   
    
    # create dataframe for time series
    df_time_series = pd.DataFrame({'Date': pd.to_datetime(dateMonth), 'PullRequests': pullReqsMonth})
    df_time_series.set_index('Date', inplace=True)

    return df_time_series


def plot_data(df):  
    plt.figure(figsize=(15, 5))
    plt.style.use('dark_background')
    # remove top and right spines
    # plt.gca().spines['top'].set_visible(False)
    # plt.gca().spines['right'].set_visible(False)
    df.plot(style='.' , figsize=(15, 5) , color = color_pal[0], title='Number of Pull Requests over time') 

def draw_bar_plot(pullReqs, date):
    plt.style.use('dark_background')
    # remove top and right spines
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.bar(date, pullReqs)
    plt.xlabel('Date')
    plt.ylabel('Number of Pull Requests')
    plt.title('Number of Pull Requests over time')
    plt.xticks(rotation=90)

    plt.show()

def split_data(df):
    train = df.loc[df.index <= '2021-12-01']
    test = df.loc[df.index > '2021-12-01']
    # train = df.loc[df.index <= '2019-12-01']
    # test = df.loc[df.index > '2019-12-01']
    return train, test


def create_features(df): 
    df = df.copy()
    df['year'] = df.index.year
    df['month'] = df.index.month
    return df

def plot_train_test(train , test):

    fig , ax = plt.subplots(figsize=(15, 5))
    plt.style.use('dark_background')
    # remove top and right spines
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    train.plot(ax=ax , style='.' , color=color_pal[0] , label = 'trainig data')  
    test.plot(ax=ax , style='.' , color=color_pal[1] , label = 'test data')
    ax.axvline('2021-12-01' , linestyle='--' , color='black' , label='train test split')
    # ax.axvline('2019-12-01' , linestyle='--' , color='black' , label='train test split')
    ax.legend(['train' , 'test' , 'train test split'])
    ax.set_title('Number of Pull Requests over time')
    plt.show()

import xgboost as xgb
from sklearn.metrics import mean_squared_error

def train_model(X_train , y_train , X_test , y_test):
    reg = xgb.XGBRegressor(n_estimators=10000 , early_stopping_rounds=50 , learning_rate=0.001)
    reg.fit(X_train , y_train , eval_set=[(X_train , y_train) , (X_test , y_test)] , verbose=100)
    return reg
















# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from statsmodels.tsa.arima.model import ARIMA
# def predict_2023_python_pull_requests(dates , pull_requests):
#     data = pd.DataFrame({'Date': pd.to_datetime(dates), 'PullRequests': pull_requests})
#     data.set_index('Date', inplace=True)

#     # Step 2: Visualize the data
#     data.plot()
#     plt.xlabel('Date')
#     plt.ylabel('Number of Pull Requests')
#     plt.title('Time Series of Pull Requests')
#     plt.show()


#         # Step 4: Fit an ARIMA model
#     model = ARIMA(data, order=(1, 1, 1))
#     model_fit = model.fit()

#     # Step 5: Validate the model
#     train_size = int(len(data) * 0.80)  # 80% of the data for training
#     train_data, test_data = data[:train_size], data[train_size:]

#     # Step 6: Forecast for 2023
#     forecast = model_fit.get_forecast(steps=len(test_data))
#     forecasted_values = forecast.predicted_mean

#     # Step 7: Visualize the forecast
#     plt.plot(data.index[:train_size], data['PullRequests'][:train_size], label='Train Data')
#     plt.plot(data.index[train_size:], data['PullRequests'][train_size:], label='Test Data')
#     plt.plot(test_data.index, forecasted_values, label='Forecast')
#     plt.xlabel('Date')
#     plt.ylabel('Number of Pull Requests')
#     plt.title('Forecast for 2023')
#     plt.legend()
#     plt.show()