import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from IPython.display import display, HTML, Markdown, Latex
import sys
sys.path.append('../')
from utils import nice_table
from tqdm import tqdm
import itertools

def basic_info(x_data):
    '''
    prints basic info about the dataset like the number of rows, columns, features.
    '''
    dic = {'Number of samples': [len(x_data)], 
           'Number of features': [len(x_data.columns)], 
           }
    display(HTML(nice_table(dic, title='Basic Counts')))


def features_info(x_data):
    '''
    prints info about the features like the type, number of unique values, missing values ratio.
    '''
    column_dict = {}
    for column in x_data.columns:  
        num_uniques = x_data[column].nunique()
        # counts nulls which were replaced by -1 or "-1" depending on the type
        num_nulls = sum(x_data[column] == -1) + sum(x_data[column] == '-1')
        nulls_ratio = round(num_nulls / len(x_data), 2)
        # outlier condition is median + 3 * IQR; lets count the number of outliers
        if type(x_data.iloc[0, x_data.columns.get_loc(column)]) == str:
            outlier_ratio = 0
        else:
            Q1, Q3 = x_data[column].quantile(0.25), x_data[column].quantile(0.75)
            iqr = Q3 - Q1
            outlier_ratio = sum(x_data[column] > Q3 + 3 * iqr) / len(x_data)
        kind = 'Categorical' if type(x_data.iloc[0, x_data.columns.get_loc(column)]) == str else 'Numerical'
        kind = 'Date' if x_data[column].dtype == 'datetime64[ns, UTC]' else kind
        kind = 'Binary' if num_uniques == 2 else kind
        kind = 'Constant' if num_uniques == 1 else kind
        kind = 'Useless' if num_uniques == 0 else kind
        kind = 'Composite' if column in ['languagesUsed', 'languagesSizes'] else kind
        
        nulls_ratio, outlier_ratio = str(round(nulls_ratio*100,2)) + '%', str(round(outlier_ratio*100,2)) + '%'
        column_dict[column] = [kind, num_uniques, nulls_ratio, outlier_ratio]
        
    display(HTML(nice_table(column_dict, title='Features Types, Uniques Count, Missing Ratio, Outlier Ratio')))




def plot_feature_histograms(x_data, sample_size):
    '''
    Plots a histogram for each feature. It gives integer labels to categorical features before plotting.
    '''
    # drop languages_used, language_sizes, and createdAt
    x_data = x_data.drop(['languagesUsed', 'languagesSizes'], axis=1)

    # get a random sample of 1000 rows
    x_data = x_data.sample(sample_size)
    # for each categorical column, factorize it
    for feat in x_data.columns:
        if type(x_data.iloc[0, x_data.columns.get_loc(feat)]) == str:
            x_data[feat] = pd.factorize(x_data[feat])[0]

    # get the number of rows and columns needed
    num_rows = len(x_data.columns) // 4 + 1
    num_cols = 4

    # increase dpi
    plt.rcParams['figure.dpi'] = 100        # increase plot resolution
    plt.style.use('dark_background')
    # make the figure
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(20, 20))

    
    # make a histogram for each feature
    for i, feat in tqdm(enumerate(x_data.columns)):
        # get the row and column index
        row, col = i // num_cols, i % num_cols
        # make the histogram
        axes[row, col].hist(x_data[feat], bins=50)
        axes[row, col].set_title(feat)
        axes[row, col].set_xlabel(feat)
        axes[row, col].set_ylabel('Frequency')
    
    # remove remaining plots
    for i in range(len(x_data.columns), num_rows * num_cols):
        fig.delaxes(axes[i // num_cols, i % num_cols])
    
    plt.show()
    

# make violin plots
def plot_violin_plots(x_data, sample_size):
    '''
    Plots violin plots for each feature. It gives integer labels to categorical features before plotting.
    '''
    # drop languages_used, language_sizes, and createdAt
    x_data = x_data.drop(['languagesUsed', 'languagesSizes', 'createdAt'], axis=1)

    # get a random sample of rows
    x_data = x_data.sample(sample_size)
    # for each categorical column, factorize it
    for feat in x_data.columns:
        if type(x_data.iloc[0, x_data.columns.get_loc(feat)]) == str:
            x_data[feat] = pd.factorize(x_data[feat])[0]

    # plot violin plots
    num_cols = 4
    num_rows = len(x_data.columns) // num_cols + 1
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(20, 20))
    for i, feat in enumerate(x_data.columns):
        col = pd.DataFrame(x_data[feat])
        sns.violinplot(col, ax=axes[i // num_cols, i % num_cols], color='#FDFD96')
    
    # remove remaining plots
    for i in range(len(x_data.columns), num_rows * num_cols):
        fig.delaxes(axes[i // num_cols, i % num_cols])
    
    plt.show()




def visualize_continuous_data(x_data, sample_size=10000):
    '''
    Plot a grid of scatter plots for each pair of continuous features.
    '''
    # get sample
    x_data = x_data.sample(sample_size)
    
    # get only the continuous features
    cont_feats = [feat for feat in x_data.columns if type(x_data.iloc[0, x_data.columns.get_loc(feat)]) != str]
    x_data_cont = x_data[cont_feats]
    # execlude the isArchived column
    x_data_cont = x_data_cont.drop('isArchived', axis=1)
    
    print("Number of continuous features:", len(x_data_cont.columns))
    
    # get all possible combinations of 2 features
    combinations = list(itertools.combinations(x_data_cont.columns, 2))
    
    num_rows = len(combinations) // 4 + 1
    num_cols = 4
     
    # plot each combination of 2 features the grid
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(20, 50))
    for i, (feat1, feat2) in tqdm(enumerate(combinations)):
        # get the row and column index
        row, col = i // num_cols, i % num_cols
        # plot the scatter plot
        axes[row, col].scatter(x_data_cont[feat1], x_data_cont[feat2], s=1)
        axes[row, col].set_xlabel(feat1)
        axes[row, col].set_ylabel(feat2)
        axes[row, col].set_title(feat1 + " vs " + feat2)
    
    # remove remaining plots
    for i in range(len(combinations), num_rows * num_cols):
        fig.delaxes(axes[i // num_cols, i % num_cols])
        
    plt.show()
    
    

def convey_insights(bullets_arr, title="Insights"):
    '''
    Give it a bullet points array, give you bullet points in markdown for insights.
    '''
    # make a markdown string with the bullets
    markdown_str = f'<h3><font color="pink" size=5>{title}</font></h3> <font size=4>\n'
    
    for bullet in bullets_arr:
        markdown_str += '<font color="pink">✦</font> ' + bullet + '<br><br>'
    # display the markdown string
    markdown_str += '</font>'
    display(Markdown(markdown_str))

def correlation_matrix(x_data, sample_size=10000):
    '''
    Plot a correlation matrix for continuous features.
    '''

    # Get sample
    x_data = x_data.sample(sample_size)

    # Get only the continuous features
    cont_feats = [feat for feat in x_data.columns if type(x_data.iloc[0, x_data.columns.get_loc(feat)]) != str]
    x_data_cont = x_data[cont_feats]
    # Execlude the isArchived column
    x_data_cont = x_data_cont.drop('isArchived', axis=1)
    # Calculate the correlation matrix
    corr_matrix = x_data_cont.corr()

    # Plot the correlation matrix as a heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, cmap="RdBu_r", fmt='.2f', linewidths=0.5, center=0, vmin=-1, vmax=1)
    plt.title("Correlation Matrix of Numerical Features")
    plt.show()
