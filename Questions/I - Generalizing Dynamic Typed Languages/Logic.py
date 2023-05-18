import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import random

dynamic_languages = ['Python', 'JavaScript', 'Ruby', 'PHP', 'Perl']
static_languages = ['Java', 'C++', 'C#', 'Go', 'TypeScript']


def preprocess_dataset(ds):
    '''
        This functions is responsible for two things:
            1- dropping useless rows (i.e. primaryLanguage is '-1' and languaesUsed is empty string)
            2- parsing the languagesUsed column into a list of languages instead of string
            3- if primaryLanguage is '-1' and languagesUsed is not empty string, then primaryLanguage is the first language in languagesUsed
            4- if primaryLanguage is not '-1' and languagesUsed is empty string, then languagesUsed is a list containing only primaryLanguage
    '''

    new_ds = ds.copy()

    # make the createdAt column contains only the year
    new_ds['year'] = new_ds['createdAt'].apply(lambda x: x.year)
    new_ds['month'] = new_ds['createdAt'].apply(lambda x: x.month)

    # drop createdAt column
    new_ds = new_ds.drop('createdAt', axis=1)

    # drop rows where primaryLanguage is '-1' and languagesUsed is empty string
    new_ds = new_ds.drop(new_ds[(new_ds['primaryLanguage'] == '-1') & (new_ds['languagesUsed'] == '')].index)

    # parse languagesUsed column into a list of languages instead of string
    new_ds['languagesUsed'] = list(new_ds['languagesUsed'].apply(lambda x: x.split(', ')))

    # if primaryLanguage is '-1' and languagesUsed is not empty string, then primaryLanguage is the first language in languagesUsed
    new_ds.loc[(new_ds['primaryLanguage'] == '-1'), 'primaryLanguage'] = new_ds['languagesUsed'].apply(lambda x: x[0])

    # if primaryLanguage is not '-1' and languagesUsed is a list of one element which is empty string
    new_ds.loc[(new_ds['primaryLanguage'] != '-1') & (new_ds['languagesUsed'].apply(lambda x: len(x) == 1 and x[0] == '')), 'languagesUsed'] = new_ds['primaryLanguage'].apply(lambda x: [x])

    return new_ds

def display_circles(labels):
    '''
    Display a grid of circles with different colors and labels.
    '''
    # Get the number of labels
    num_labels = len(labels)
    
    # Set up a plot with 5 columns and as many rows as needed
    num_cols = 5
    num_rows = (num_labels // num_cols) + 1
    
    fig, ax = plt.subplots(num_rows, num_cols, figsize=(20, 20), frameon=False)
    fig.subplots_adjust(hspace=0, wspace=0.2)
    plt.rcParams['figure.dpi'] = 100

    # Set the font size and family
    font_size = 10
    font_family = 'sans-serif'
    
    # Set the margin for each circle
    margin = 0.05
    
    # For each label
    for i, label in enumerate(labels):
        row, col = i // num_cols, i % num_cols
        
        # Set a random color for each circle
        color = random.choice(['red', 'blue', 'green', 'orange', 'purple'])
        
        # Create the circle patch with the margin
        circle = Circle(xy=(0.5, 0.5), radius=0.5 - margin, fc=color, ec=None, lw=2)        
        # Add the circle patch to the plot
        ax[row, col].add_patch(circle)
        
        # Set the label as the text inside the circle
        ax[row, col].text(0.5, 0.5, label, horizontalalignment='center', verticalalignment='center', fontsize=font_size, c='white', fontfamily=font_family)
        
        # Set the axis limits to fit the circle
        ax[row, col].set_xlim([0, 1])
        ax[row, col].set_ylim([0, 1])
        ax[row, col].set_aspect('equal')
        
        # Remove the x and y ticks
        ax[row, col].set_xticks([])
        ax[row, col].set_yticks([])

        ax[row, col].set_facecolor('none')
        ax[row, col].set_frame_on(False)
        
    # Remove the unused plots
    for i in range(num_labels, num_rows * num_cols):
        fig.delaxes(ax[i // num_cols, i % num_cols])
    
    
    fig.subplots_adjust(hspace=0.5, wspace=0.5)  # Adjust the spacing between the rows and columns
    plt.show()

def sort_languages(ds, langs):
    '''
        sort languages passed with respect to the frequency of each language if exist if not ignore it
    '''
    # get the frequency of each language in the ds

    freq = {}
    for lang in langs:
        freq[lang] = len(ds[ds['primaryLanguage'] == lang])

    # sort the languages with respect to the frequency
    sorted_langs = sorted(freq, key=freq.get, reverse=True)

    return sorted_langs

def get_frequncy_of_languages(ds, kind='all'):
    '''
        get the frequency of each language in the ds
    '''
    freq = {}
    for lang in ds['primaryLanguage']:
        if kind == 'dynamic' and lang not in dynamic_languages or kind == 'static' and lang not in static_languages:
            continue
        if lang in freq:
            freq[lang] += 1
        else:
            freq[lang] = 1

    langs = []
    freqs = []

    for lang, f in freq.items():
        langs.append(lang)
        freqs.append(f)

    return langs, freqs

def show_pie(labels, freqs, title, show=True):
    '''
        show pie chart for the frequency of each language
    '''
    freqs = freqs[:6]
    labels = labels[:6]
    plt.rcParams['figure.figsize'] = [20, 10]
    plt.rcParams['figure.dpi'] = 100
    plt.style.use('dark_background')
    plt.pie(freqs, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 14, 'color': 'white'})
    plt.title(title)
    plt.axis('equal')
    if show:
        plt.show()

def split_dataset_across_years(ds):
    '''
    Input: dataset
    Output: two lists of datasets, one list for dynamic languages and the other for static languages
    and each list contains datasets for each year
    '''
    dynamic_datasets = {}
    static_datasets = {}

    # get years present in the dataset
    years = ds['year'].unique()

    # split the dataset into two datasets, one for dynamic languages and the other for static languages
    for year in years:
        dynamic_datasets[year] = ds[(ds['year'] == year) & (ds['primaryLanguage'].isin(dynamic_languages))]
        static_datasets[year] = ds[(ds['year'] == year) & (ds['primaryLanguage'].isin(static_languages))]

    return dynamic_datasets, static_datasets

def split_dataset_across_years_months(ds):
    '''
    Input: dataset
    Output: two lists of datasets, one list for dynamic languages and the other for static languages
    and each list contains datasets for each year
    '''
    dynamic_datasets = {}
    static_datasets = {}

    # get years present in the dataset
    years = ds['year'].unique()

    # split the dataset into two datasets, one for dynamic languages and the other for static languages
    for year in years:
        dynamic_datasets[year] = {}
        static_datasets[year] = {}
        for month in range(1, 13):
            dynamic_datasets[year][month] = ds[(ds['year'] == year) & (ds['month'] == month) & (ds['primaryLanguage'].isin(dynamic_languages))]
            static_datasets[year][month] = ds[(ds['year'] == year) & (ds['month'] == month) & (ds['primaryLanguage'].isin(static_languages))]

    return dynamic_datasets, static_datasets


def show_pie_chart_for_each_year(dynamic_datasets, static_datasets):
    '''
        show pie chart for each year to show the usage of dynamic and static languages 
    '''

    # union of the years of dynamic and static datasets
    years = list(set(dynamic_datasets.keys()) | set(static_datasets.keys()))
    years.sort()
    years = years[-9:]
    plt.rcParams['figure.figsize'] = [20, 10]
    for i, year in enumerate(years):

        plt.subplot(3, 3, i+1)

        # get the frequency of each language in the dynamic datasets
        _, dynamic_freqs = get_frequncy_of_languages(dynamic_datasets[year])
        # get the frequency of each language in the static datasets
        _, static_freqs = get_frequncy_of_languages(static_datasets[year])

        show_pie(['dynamic','static'], [sum(dynamic_freqs), sum(static_freqs)], f'Year {year}', show=False)

    plt.show()


