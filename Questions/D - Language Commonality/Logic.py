### contains implementations for functions to be used (directly called) in the notebook
import pandas as pd
def explore_primary_languages(ds):
    '''
    Given a dataset, it returns a dataframe with the top_n primary languages and their counts.
    '''
    # get the unique languages
    unique_langs = ds['primaryLanguage'].unique()



    return unique_langs

def get_top_used_languages_with_counts(ds, top_n , plot = True):
    ds = ds.copy()
    ds = ds[ds['primaryLanguage'] != '-1']
    # get the counts of each language
    lang_counts = ds['primaryLanguage'].value_counts()
    # make a dataframe
    lang_counts = pd.DataFrame({'language': lang_counts.index, 'count': lang_counts.values})
    # get the top_n languages
    top_langs = lang_counts.iloc[:top_n, :]
    if plot:
        plot_top_n_languages(ds, top_n , top_langs)

    return top_langs 

def get_margins(ds):
    first = get_top_used_languages_with_counts(ds, 1 , False)
    first = first.iloc[0, 1]
    second = get_top_used_languages_with_counts(ds, 2 , False)
    second = second.iloc[1, 1]
    third = get_top_used_languages_with_counts(ds, 3 , False)
    third = third.iloc[2, 1]

    return first - second , second - third

import matplotlib.pyplot as plt
def plot_top_n_languages(ds, top_n , top_langs):
    # make bar plot for the top_n languages
    plt.bar(top_langs['language'], top_langs['count'])
    plt.xlabel('Language')
    plt.ylabel('Count')
    plt.title('Top ' + str(top_n) + ' languages used in Github repositories')
    plt.show()



