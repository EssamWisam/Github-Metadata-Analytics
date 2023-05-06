### contains implementations for functions to be used (directly called) in the notebook

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def preprocess_languages_column(data):
    # remove rows with missing values in primaryLanguage
    data = data[data['primaryLanguage'] != '-1']
    
    # filter out rows with missing values in languagesUsed and languagesSizes
    data = data[data['languagesUsed'].notna() & data['languagesSizes'].notna()]

    # split languagesSizes and convert to float
    data['languagesSizes'] = data['languagesSizes'].apply(lambda x: [float(s) for s in str(x).split(', ') if s != ''])
    
    # split languagesUsed and filter out None and empty strings
    data['languagesUsed'] = data['languagesUsed'].apply(lambda x: [s for s in str(x).split(', ') if s != 'None' and s != ''])

    return data


def visualize(map_year_data):

    # for each year, plot the top 3 languages in a bar chart

    for year in map_year_data:
        print(map_year_data[year])

        programming_langs = map_year_data[year]['language'].tolist()
    
        # avg disk usage for each language
        avg_disk_usage = map_year_data[year]['average diskUsageKb'].tolist()

        # total pull requests for each language
        total_prs = map_year_data[year]['total pullRequests'].tolist()

        # plot the bar chart
        plt.figure(figsize=(10, 5))
        plt.bar(programming_langs, avg_disk_usage, color='blue', width=0.4)
        plt.bar(programming_langs, total_prs, color='red', width=0.4)
        plt.xlabel('Programming Languages')
        plt.ylabel('Average Disk Usage (KB)')
        plt.title('Average Disk Usage vs Total Pull Requests for Top 3 Programming Languages in ' + str(year))
        plt.legend(['Average Disk Usage', 'Total Pull Requests'])
        plt.show()





    

def get_top_k_programming_languages_over_time(data, k):
    ''''
    split the data into years and get the top k programming languages for each year
    '''

    # make copy of the dataframe
    data = data.copy()

    map_year_data = {}

    # loop over data and split it into years
    for year in data['createdAt'].dt.year.unique():
        map_year_data[year] = get_top_k_programming_languages_per_year(data[data['createdAt'].dt.year == year], k)


    return map_year_data



def get_top_k_programming_languages_per_year(data, k):
    '''
    Given a dataframe, it returns the top k programming languages used in the repositories. with average disk usage.
    returns list of tuples (language, [number of pull requests, disk usage])
    '''

    # make copy of the dataframe
    data = data.copy()

    # data = preprocess_languages_column(data)

    language_prs = {}

    for i in range(len(data)):
        
        primary_lang    = data.iloc[i]['primaryLanguage']
        prs             = data.iloc[i]['pullRequests']    
        languages_used  = data.iloc[i]['languagesUsed']
        languages_sizes = data.iloc[i]['languagesSizes']

        if len(languages_used) == 0 or len(languages_sizes) != len(languages_used):
            continue

        index = -1
        for i in range(len(languages_used)):
            if languages_used[i] == primary_lang:
                index = i
                break
        
        if index == -1:
            continue
 
        # get the size of the primary language
        primary_lang_size = languages_sizes[index]

        
        if primary_lang in language_prs:
            language_prs[primary_lang][0] += prs
            language_prs[primary_lang][1] += (primary_lang_size / 1024)
        else:
            language_prs[primary_lang] = [prs, primary_lang_size]


    # sort the languages by number of pull requests
    top_languages = sorted(language_prs.items(), key=lambda item: item[1][0], reverse=True)

    # calculate the average disk usage
    for i in range(min(k, len(top_languages))):
        top_languages[i][1][1] /= data['primaryLanguage'].value_counts()[top_languages[i][0]]

    # create an empty dataframe with three columns: language, total pull requests, average disk usage
    top_languages_df = pd.DataFrame(columns=['language', 'total pullRequests', 'average diskUsageKb'])

    # fill the dataframe with the top k languages
    for i in range(min(k, len(top_languages))):
        top_languages_df.loc[i] = [top_languages[i][0], top_languages[i][1][0], top_languages[i][1][1]]


    return top_languages_df




