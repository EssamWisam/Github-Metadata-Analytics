### contains implementations for functions to be used (directly called) in the notebook


def preprocess_data(df):
    data = df.copy()
    data = data.drop(['stars', 'forks', 'watchers', 'isArchived', 'pullRequests', 'createdAt', 'defaultBranchCommitCount', 'assignableUserCount', 'codeOfConduct'], axis=1)

    return data
    
def explore_primary_languages_and_sizes(df):
    unique_langs = df['primaryLanguage'].unique()
    unique_license = df['license'].unique()
    unique_size = df['diskUsageKb'].unique()

    max_size = df['diskUsageKb'].max()
    min_size = df['diskUsageKb'].min()
    std_size = df['diskUsageKb'].std()

    return unique_langs , unique_license , max_size , min_size , std_size

import matplotlib.pyplot as plt

def preprocess_data_for_plotting(df):
    df = df.copy()
    df = df.dropna(subset=['license', 'diskUsageKb'])
    df = df[df['license'] != '-1']
    df = df[df['primaryLanguage'] != '-1']
    lang_counts = df['primaryLanguage'].value_counts()
    # make a dataframe
    lang_counts = pd.DataFrame({'language': lang_counts.index, 'count': lang_counts.values})
    # get the top_n languages
    top_n = 10
    top_langs = lang_counts.iloc[:top_n, :]

    license_counts = df['license'].value_counts()
    # make a dataframe
    license_counts = pd.DataFrame({'license': license_counts.index, 'count': license_counts.values})
    # get the top_n licenses
    top_n = 10
    top_licenses = license_counts.iloc[:top_n, :]

    df_filtered = df[df['primaryLanguage'].isin(top_langs['language']) & df['license'].isin(top_licenses['license'])]

    return df_filtered

import numpy as np
def plot_top_n_languages(df):
    df = preprocess_data_for_plotting(df)
    counts= df.groupby(['primaryLanguage'])['primaryLanguage'].count()
    counts = counts.sort_values(ascending=False)
    plt.bar(counts.index, counts.values)
    plt.xlabel('Language')
    xticks = counts.index
    plt.xticks(xticks, rotation=90)
    plt.ylabel('Count')
    plt.title('Top languages used in Github repositories')
    plt.show()

def plot_top_n_licenses(df):
    df = preprocess_data_for_plotting(df)
    counts= df.groupby(['license'])['license'].count()
    counts = counts.sort_values(ascending=False)
    plt.bar(counts.index, counts.values)
    plt.xlabel('License')
    xticks = counts.index
    plt.xticks(xticks, rotation=90)
    plt.ylabel('Count')
    plt.title('Top licenses used in Github repositories')
    plt.show()
   

import seaborn as sns
def plot_diskUsages(df):
    df = preprocess_data_for_plotting(df)
    plt.figure(figsize=(20, 10))
    sns.distplot(df['diskUsageKb'])
    plt.xlabel('Project Size (KB)')
    plt.ylabel('Density')
    plt.title('Distribution of Project Sizes')
    plt.show()

    


def plot_license_with_project_size(df):
    df = preprocess_data_for_plotting(df)
    plt.figure(figsize=(20, 10))
    plt.scatter(df['license'], df['diskUsageKb'], c=df.groupby(['license' , 'diskUsageKb'])['license'].transform('count'), cmap='viridis')
    plt.xlabel('License')
    plt.ylabel('Project Size (KB)')
    plt.title('Project Size vs License')
    plt.colorbar(label='Number of Occurrences')
    plt.show()



def plot_licence_with_language(df):
    df = preprocess_data_for_plotting(df)
    plt.figure(figsize=(20, 10))
    plt.scatter(df['license'], df['primaryLanguage'], c=df.groupby(['license' , 'primaryLanguage'])['license'].transform('count'), cmap='viridis')
    plt.xlabel('License')
    plt.ylabel('Language')
    plt.title('Language vs License')
    plt.show()

def plot_project_size_with_language(df):
    df = preprocess_data_for_plotting(df)
    plt.figure(figsize=(20, 10))
    plt.scatter(df['diskUsageKb'], df['primaryLanguage'], c=df.groupby(['primaryLanguage' , 'diskUsageKb'])['primaryLanguage'].transform('count'), cmap='viridis')
    plt.xlabel('Project Size (KB)')
    plt.ylabel('Language')
    plt.title('Language vs Project Size')
    plt.show()

def get_statistics_for_license_with_disk_usage(df):
    # get only rows with diskUsageKb > 30kb
    new_df = df.copy()
    new_df = df[df['diskUsageKb'] > 10000]

    # get how many rows of them have license
    df_with_license = new_df[new_df['license'] != '-1']

    print('Number of repositories with license: ', len(df_with_license))
    print('Number of repositories without license: ', len(new_df) - len(df_with_license))

    percentage = len(df_with_license) / len(df) * 100

    print('Percentage of repositories with license: ', percentage)

    new_df = df.copy()

    # get only rows with diskUsageKb < 30kb & > 15kb
    new_df = df[df['diskUsageKb'] < 30]
    
    new_df = new_df[new_df['diskUsageKb'] > 15]

    # get how many rows of them have license

    df_with_license = new_df[new_df['license'] != '-1']

    print('Number of repositories with license: ', len(df_with_license))
    print('Number of repositories without license: ', len(new_df) - len(df_with_license))

    percentage = len(df_with_license) / len(new_df) * 100

    print('Percentage of repositories with license: ', percentage)

    percentages = [] 
    x_axis = []
    step = 1000
    max_size = 300000 #df['diskUsageKb'].max()

    print(max_size)
    for i in range (max_size , 0 , -step):
        new_df = df.copy()
        new_df = df[df['diskUsageKb'] > i]
        new_df = new_df[new_df['diskUsageKb'] < i + step]
        df_with_license = new_df[new_df['license'] != '-1']
        if len(new_df) == 0:
            continue
        percentage = len(df_with_license) / len(new_df) * 100
        x_axis.append(i)
        percentages.append(percentage)

    plt.figure(figsize=(20, 10))
    plt.plot(x_axis, percentages)
    plt.xlabel('Project Size (KB)')
    plt.ylabel('Percentage of repositories with license')
    plt.title('Percentage of repositories with license vs Project Size')
    plt.show()



def get_statistics_for_language_with_disk_usage(df , language):
    x_axis = []
    diskUsages = []
    index = 0
    for row in df.itertuples():
        if row.primaryLanguage == language:
            x_axis.append(index)
            diskUsages.append(row.diskUsageKb)
            index += 1

    plt.figure(figsize=(20, 10))
    plt.plot(x_axis, diskUsages)
    plt.xlabel('language seen in the dataset')
    plt.ylabel('Project Size (KB)')
    plt.title('language vs Project Size')
    plt.show()

def get_statistics_for_language_with_licence(df , language):
    x_axis = []
    licenses = []
    index = 0
    for row in df.itertuples():
        if row.primaryLanguage == language:
            x_axis.append(index)
            licenses.append(row.license)
            index += 1

    plt.figure(figsize=(20, 10))
    plt.plot(x_axis, licenses)
    plt.xlabel('language seen in the dataset')
    plt.ylabel('License')
    plt.title('language vs License')
    plt.show()


# def plot_project_size_with_license_with_language(df):
#     plt.figure(figsize=(20, 10))
#     plt.scatter(df['diskUsageKb'], df['license'] , c = df['primaryLanguage'])
#     plt.xlabel('Project Size (KB)')
#     plt.ylabel('License')
#     plt.title('License vs Project Size')
#     plt.show()
import pandas as pd
# def plot_project_size_with_license_with_language_3D(df):
#     # drop null values in license , primaryLanguage and diskUsageKb
#     df = df.dropna(subset=['license', 'primaryLanguage', 'diskUsageKb'])
#     df = df[df['primaryLanguage'] != '-1']
#     # get the counts of each language
#     lang_counts = df['primaryLanguage'].value_counts()
#     # make a dataframe
#     lang_counts = pd.DataFrame({'language': lang_counts.index, 'count': lang_counts.values})
#     # get the top_n languages
#     top_n = 10
#     top_langs = lang_counts.iloc[:top_n, :]


#     license_counts = df['license'].value_counts()
#     # make a dataframe
#     license_counts = pd.DataFrame({'license': license_counts.index, 'count': license_counts.values})
#     # get the top_n licenses
#     top_n = 10
#     top_licenses = license_counts.iloc[:top_n, :]


#     df_filtered = df[df['primaryLanguage'].isin(top_langs['language']) & df['license'].isin(top_licenses['license'])]
#     # plot top 10 languages and top 10 licenses with project size
#     fig = plt.figure(figsize=(20, 10))
#     ax = fig.add_subplot(111, projection='3d')
#     ax.scatter(df_filtered['primaryLanguage'], df_filtered['license'], df_filtered['diskUsageKb'])
#     ax.set_xlabel('Language')
#     ax.set_ylabel('License')
#     ax.set_zlabel('Project Size (KB)')
#     plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import LabelEncoder

def plot_project_size_with_license_with_language(df):
    # drop null values in license, primaryLanguage, and diskUsageKb
    df_filtered = df.dropna(subset=['license', 'primaryLanguage', 'diskUsageKb'])
    # create a new column for project size in MB
    df_filtered['diskUsageMb'] = df_filtered['diskUsageKb'] / 1024
    # group by license, primaryLanguage, and diskUsageMb and count the number of projects
    df_grouped = df_filtered.groupby(['license', 'primaryLanguage', 'diskUsageMb'], as_index=False)['id'].count()
    # plot the data
    plt.figure(figsize=(20, 10))
    plt.scatter(df_grouped['diskUsageMb'], df_grouped['license'], c=df_grouped['primaryLanguage_enc'])
    plt.xlabel('Project Size (MB)')
    plt.ylabel('License')
    plt.title('License vs Project Size')
    plt.colorbar(label='Primary Language')
    plt.show()

def plot_project_size_with_license_with_language_3D(df):
    # drop null values in license, primaryLanguage, and diskUsageKb
    df_filtered = df.dropna(subset=['license', 'primaryLanguage', 'diskUsageKb'])
    # create a new column for project size in MB
    df_filtered['diskUsageMb'] = df_filtered['diskUsageKb'] / 1024
    # encode the primaryLanguage and license columns
    le = LabelEncoder()
    df_filtered['primaryLanguage_enc'] = le.fit_transform(df_filtered['primaryLanguage'])
    df_filtered['license_enc'] = le.fit_transform(df_filtered['license'])
    # group by primaryLanguage_enc, license_enc, and diskUsageMb and count the number of projects
    df_grouped = df_filtered.groupby(['primaryLanguage_enc', 'license_enc', 'diskUsageMb'], as_index=False)['id'].count()
    # get the top 10 primary languages and licenses by project count
    top_langs = df_filtered['primaryLanguage'].value_counts().nlargest(10).index.tolist()
    top_licenses = df_filtered['license'].value_counts().nlargest(10).index.tolist()
    # filter the data to include only the top languages and licenses
    df_top = df_grouped[df_grouped['primaryLanguage_enc'].isin(top_langs) & df_grouped['license_enc'].isin(top_licenses)]
    # create the 3D plot
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df_top['primaryLanguage_enc'], df_top['license_enc'], df_top['diskUsageMb'], c=df_top['diskUsageMb'])
    ax.set_xlabel('Primary Language')
    ax.set_ylabel('License')
    ax.set_zlabel('Project Size (MB)')
    ax.set_xticklabels(le.inverse_transform(ax.get_xticks()).tolist())
    ax.set_yticklabels(le.inverse_transform(ax.get_yticks()).tolist())
    plt.show()
