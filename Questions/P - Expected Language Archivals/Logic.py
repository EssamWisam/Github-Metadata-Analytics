import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def archival_overtime(x_data_d):
    '''
    For each year from 2009 to 2023 find the number and fraction of archivals for each language and return the result in a flat array.
    '''
    x_data_t = []
    # Make a dataset for each year
    for year in range(2009, 2023):
        # Get the data for that year
        x_data = x_data_d[x_data_d['year'] == year]
        # Get the unique languages
        langs = x_data['primaryLanguage'].unique()
        if '-1' in langs: langs = langs[langs != '-1']
        # For each language
        for lang in langs:
            # Get the data for that language
            lang_data = x_data[x_data['primaryLanguage'] == lang]
            # Get the number of repos in that language
            num_lang_repos = len(lang_data)
            # Get the number of repos in that language with isArchived = 1
            num_archived_lang_repos = len(lang_data[lang_data['isArchived'] == 1])
            # Get the fraction of repos in that language with isArchived = 1
            frac_archived_lang_repos = num_archived_lang_repos / num_lang_repos
            # Append the data to the 
            x_data_t.append([year, lang, num_lang_repos, num_archived_lang_repos, frac_archived_lang_repos])
    x_data_t = pd.DataFrame(x_data_t, columns=['year', 'language', 'num_lang_repos', 'num_archived_lang_repos', 'frac_archived_lang_repos'])
    return x_data_t


# Now for each year let's find the most archived languages
def most_archived_langs(x_data_t, exc_docker=True):
    '''
    Given the fraction of archivals for each language for each yeat from 2009 to 2023, find the most archived language for each year.
    '''
    # drop any row with less than 50 language repos
    if exc_docker:
        x_data_t = x_data_t[x_data_t['language'] != 'Dockerfile']
    x_data_t = x_data_t[x_data_t['num_lang_repos'] >= 50]
    x_data_t = x_data_t.sort_values(by='frac_archived_lang_repos', ascending=False)
    x_data_t = x_data_t.drop_duplicates(subset='year', keep='first')    # keeping the first yields the most archived.
    x_data_t = x_data_t.sort_values(by='year')
    return x_data_t


# Plot the data in a line plot where the language is written on each point and the x-axis is year, y-axis is frac_archived_lang_repos
def plot_most_archived_per_year(x_data_t):
    '''
    Plot the most archived language per year.
    '''
    # dark mode
    plt.rcParams['figure.dpi'] = 150
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.plot(x_data_t['year'], x_data_t['frac_archived_lang_repos'], marker='o', color='aquamarine')
    for i, lang_name in enumerate(x_data_t['language']):
        ax.annotate(lang_name, (x_data_t['year'].iloc[i] + 0.15, -0.001 + x_data_t['frac_archived_lang_repos'].iloc[i]))

    ax.set_xlabel('Year')
    ax.set_ylabel('Fraction of Archived Repositories')
    ax.set_title('Most Archived Language Over Time')
    ax.set_xticks(x_data_t['year'])
    ax.set_xticklabels(x_data_t['year'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks(rotation=90)
    plt.show()
    
    
    

def archival_overtime_given_lang(x_data_d, lang, unit='month'):
    '''
    Find the yearly or monthly number of archives for a given language
    '''
    if unit == 'month':
        x_data_t = []
        # Make a dataset for each year
        for year in range(2009, 2023):
            x_data = x_data_d[x_data_d['year'] == year]
            for month in range(1, 13):
                x_data_m = x_data[x_data['month'] == month]            
                # Get the rows with the language
                x_data_m = x_data_m[x_data_m['primaryLanguage'] == lang]
                # Count the number of archives
                num_archives = len(x_data_m[x_data_m['isArchived'] == 1])
                # Count the number of repos
                num_repos = len(x_data_m)
                if len(x_data_m) == 0:    
                    frac_archives = 0
                # Append the data to the list
                else:
                    frac_archives = num_archives / num_repos
                x_data_t.append([year, month, num_archives, num_repos, frac_archives])
        return pd.DataFrame(x_data_t, columns=['year', 'month', 'num_archives', 'num_repos', 'frac_archives'])
    else:
        x_data_t = []
        # Make a dataset for each year
        for year in range(2009, 2023):
            x_data = x_data_d[x_data_d['year'] == year]
            # Get the rows with the language
            x_data = x_data[x_data['primaryLanguage'] == lang]
            # Count the number of archives
            num_archives = len(x_data[x_data['isArchived'] == 1])
            # Count the number of repos
            num_repos = len(x_data)
            # Append the data to the list
            frac_archives = num_archives / num_repos
            x_data_t.append([year, num_archives, num_repos, frac_archives])
        return pd.DataFrame(x_data_t, columns=['year', 'num_archives', 'num_repos', 'frac_archives'])



# Make a plot for the number of archivals per month for python vs year-month
def plot_archivals_per_month(x_data_lang, lang_name, k=None):
    '''
    Plot the number of archivals per month for python vs year-month for the last k years
    '''
    x_data_p = x_data_lang.copy()
    if k is not None:
        x_data_p['year-month'] = x_data_p['year'].astype(str) + '-' + x_data_p['month'].astype(str)
        x_data_p = x_data_p[x_data_p['year'] >= 2023 - k]
    else:
        x_data_p['index'] = [i for i in range(len(x_data_p))]
        k = 2023 - 2009
        
    # set darkgrid style
    plt.style.use('dark_background')
    # increase dpi
    plt.rcParams['figure.dpi'] = 150
    fig, ax = plt.subplots(figsize=(15, 7))
    if k <= 8:
        ax.plot(x_data_p['year-month'], x_data_p['frac_archives'], marker='o', color='aquamarine')
    else:
        ax.plot(x_data_p['index'], x_data_p['num_archives'], marker='o', color='aquamarine')
    ax.set_xlabel('Year-Month')
    ax.set_ylabel('Number of Archived Repositories')
    if k <= 8:
        ax.set_xticks(x_data_p['year-month'])
        ax.set_xticklabels(x_data_p['year-month'], rotation=90)
        ax.tick_params(axis='x', labelsize=6)
    else:
        ax.set_xticks(x_data_p['index'])
        ax.set_xticklabels(x_data_p['index'], rotation=90)
        ax.tick_params(axis='x', labelsize=4)
    ax.set_title(f'Number of Archived {lang_name} Repositories Over Time')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.show()




def train_test_timesplit(x_data_lang, split_date='2021-01-01'):

    # set 'year_month' column as the index
    x_data_lang['year_month'] = pd.to_datetime(x_data_lang['year'].astype(str) + '-' + x_data_lang['month'].astype(str))
    x_data_lang = x_data_lang.set_index('year_month')
    
    # keep only the 'year', 'month', and 'frac_archives' columns
    x_data_lang = x_data_lang[['year', 'month', 'frac_archives']]
    
    # split data into training and valing sets
    if split_date is not None:
        train_data = x_data_lang[:split_date]
        val_data = x_data_lang[split_date:]
    else:
        train_data = x_data_lang

    # prepare training and valing data
    x_train, y_train = train_data.drop('frac_archives', axis=1), train_data['frac_archives']
    
    if split_date is not None:
        x_val, y_val = val_data.drop('frac_archives', axis=1), val_data['frac_archives']
    else:
        x_val, y_val = None, None
        
    return x_train, y_train, x_val, y_val


# Let's make a plot of 6 columns and as much rows as needed
def plot_timeperformance(lang_preds, susp_list):
    '''
    Plot the training and validation data for each of the languages
    '''
    n_cols = 3
    n_rows = int(np.ceil(len(susp_list) / n_cols))
    fig, axs = plt.subplots(n_rows, n_cols, figsize=(20, 20))
    avg_rmses = round(np.mean([lang_preds[lang]["rmse"] for lang in susp_list]), 5)
    fig.suptitle(f'Time Prediction Over Languages Average RMSE: {avg_rmses}', fontsize=14)
    fig.tight_layout(pad=3.0)
    for i, lang in enumerate(susp_list):
        axs[i // n_cols, i % n_cols].plot(lang_preds[lang]["x_train"].index, lang_preds[lang]["y_train"], label='y_train')
        axs[i // n_cols, i % n_cols].plot(lang_preds[lang]["x_train"].index, lang_preds[lang]["train_pred"], label='y_train_preds')
        axs[i // n_cols, i % n_cols].plot(lang_preds[lang]["x_val"].index, lang_preds[lang]["y_val"], label='y_val')
        axs[i // n_cols, i % n_cols].plot(lang_preds[lang]["x_val"].index, lang_preds[lang]["val_pred"], label='y_val_preds')
        axs[i // n_cols, i % n_cols].set_title(f'{lang} Language RMSE: %.4f'% lang_preds[lang]["rmse"])
        axs[i // n_cols, i % n_cols].spines['top'].set_visible(False)
        axs[i // n_cols, i % n_cols].spines['right'].set_visible(False)
        axs[i // n_cols, i % n_cols].legend(prop={'size': 5})
        fig.subplots_adjust(hspace=0.5)

    if len(susp_list) % n_cols != 0:
        for i in range(len(susp_list) % n_cols, n_cols):
            fig.delaxes(axs[n_rows - 1, i])

    plt.show()


def plot_future_2023(lang_archives_2023):
    '''
    Plot the average number of archivals for each language in 2023
    '''
    # Now plot a bar chart of the average number of archivals for each language
    plt.rcParams['figure.dpi'] = 150
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(15, 7))

    lang_archives_2023 = {k: v for k, v in sorted(lang_archives_2023.items(), key=lambda item: item[1], reverse=True)}
    ax.bar(lang_archives_2023.keys(), lang_archives_2023.values(), color='LemonChiffon')
        
    ax.set_xlabel('Programming Language')
    ax.set_ylabel('Average Fraction of Archived Repositories')
    ax.set_title('Average Fraction of Archived Repositories for Each Programming Language in 2023')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks(rotation=90)
    plt.show()

def get_suspect_langs(x_data_t):
    # Find the top archived languages for 2022
    x_data_t_year = x_data_t[x_data_t['year'] == 2021]
    x_data_t_year = x_data_t_year.sort_values(by='frac_archived_lang_repos', ascending=False)
    x_data_t_year = x_data_t_year[x_data_t_year['num_lang_repos'] >= 50]
    x_data_t_year = x_data_t_year[x_data_t_year['language'] != 'Dockerfile']
    x_data_t_year = x_data_t_year[x_data_t_year['language'] != '-1']
    x_data_t_year = x_data_t_year.sort_values(by='frac_archived_lang_repos', ascending=False)
    x_data_t_year

    # execlude any language with less than 3 archived repos
    x_data_t2022 = x_data_t_year[x_data_t_year['num_archived_lang_repos'] >= 3]
    # get all languages in this
    suspected_langs = x_data_t2022['language'].unique()
    return list(suspected_langs)