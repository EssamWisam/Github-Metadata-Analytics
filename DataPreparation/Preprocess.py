import os
import matplotlib.pyplot as plt
import itertools
import pandas as pd
import numpy as np
import seaborn as sns
from IPython.display import display, HTML, Markdown, Latex
import sys
import ast
# sys.path.append('../')
# from utils import nice_table
sys.path.append('../')
#from utils import nice_table
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor

def split_script():
    '''
    Running this script will split the dataset into train, val, and test sets with ratio 70:20:10. For consistent 
    results do not change the random state from 42.
    '''
    # read the data
    module_dir = os.path.dirname(__file__)
    ds = pd.read_csv(os.path.join(module_dir, '../DataFiles/dataset.csv'))

    # randomly shuffle the data
    ds = ds.sample(frac=1, random_state=42).reset_index(drop=True)

    # random split the test into 70% train, 20% val, 10% test
    train, val, test = np.split(ds.sample(frac=1, random_state=42), [int(.7*len(ds)), int(.9*len(ds))])

    # save the data
    train.to_csv('../DataFiles/train.csv', index=False)
    val.to_csv('../DataFiles/val.csv', index=False)
    test.to_csv('../DataFiles/test.csv', index=False)


def read_data(kind=None, y_data_col=None, execlude=[], split="train", fix=False, handle_langs=False, handle_useless=""):
    '''
    reads the dataset from the folder and return it; if data is not split (only dataset.csv exists), it splits it first.
    If kind is specified, it returns only the categorical or numerical features.
    y_data_col allows extracting a specific column into y_data. If not specified, y_data is None.
    execlude allows excluding specific columns from the dataset.
    fix fixes any issies in the dataset, for a per-issue decisions, consider the rest of the parameters.
    '''
    module_dir = os.path.dirname(__file__)
    # if there exists not a train, val or test file, split the dataset
    if not os.path.exists(os.path.join(module_dir, '../DataFiles/train.csv')) and not os.path.exists(os.path.join(module_dir, '../DataFiles/val.csv')) and not os.path.exists(os.path.join(module_dir, '../DataFiles/test.csv')):
        split_script()
    
    if split == "train":    path = os.path.join(module_dir, '../DataFiles/train.csv')
    elif split == "val":    path = os.path.join(module_dir, '../DataFiles/val.csv')
    elif split == "test":   path = os.path.join(module_dir, '../DataFiles/test.csv')
    elif split == "all":   path = os.path.join(module_dir, '../DataFiles/dataset.csv')
    
    # read
    ds = pd.read_csv(path)
    
    # let missing values be -1 or "-1" as a temporary handling depending on column type
    for col in ds.columns:
        if type(ds.iloc[0, ds.columns.get_loc(col)]) == str:
            ds[col] = ds[col].fillna("-1")
        else:
            ds[col] = ds[col].fillna(-1)
        
    # cast codeOfConduct to string
    ds['codeOfConduct'] = ds['codeOfConduct'].astype(str)
    # cast createdAt to datetime
    ds['createdAt'] = pd.to_datetime(ds['createdAt'])
    # cast isArchived, defaultBranchCommitCount
    ds['isArchived'] = ds['isArchived'].astype(int)
    # cast isForked to int
    ds['isFork'] = ds['isFork'].astype(int)
    # cast forkingAllowed to int
    ds['forkingAllowed'] = ds['forkingAllowed'].astype(int)
    
    if handle_useless == "all-except-description":
        ds = ds.drop(['isFork', 'forkingAllowed', 'parent', 'owner', 'name', 'nameWithOwner', 'pushedAt'], axis=1) 
    elif handle_useless == "obvious":
        # drop useless columns
        ds = ds.drop(['owner', 'name', 'nameWithOwner', 'description', 'pushedAt'], axis=1)         # won't be used
    elif handle_useless == "all" or fix:    
        # drop constant or nan columns
        ds = ds.drop(['isFork', 'forkingAllowed', 'parent', 'owner', 'name', 'nameWithOwner', 'description', 'pushedAt'], axis=1)         # won't be used
    
    if handle_langs or fix:
        # handle the languages column
        ds = handle_languages_column(ds)
    
    if y_data_col:
        # all columns except Body_Level go to x_data
        x_data = ds.drop(y_data_col, axis=1)
        y_data = ds[y_data_col]
    else:
        x_data = ds
        y_data = None
    
    if kind == "Categorical":
        # extract only the categorical features
        disc_feats = [feat for feat in x_data.columns if type(x_data.iloc[0, x_data.columns.get_loc(feat)]) == str]
        x_data = x_data[disc_feats]
        
    elif kind == "Numerical":
        # extract only the numerical features
        cont_feats = [feat for feat in x_data.columns if type(x_data.iloc[0, x_data.columns.get_loc(feat)]) != str]
        x_data = x_data[cont_feats]
        for feat in x_data.columns:
            x_data[feat] = x_data[feat].astype(float)
    
    if execlude:
        x_data = x_data.drop(execlude, axis=1)

    return x_data, y_data



def handle_languages_column(x_data):
    '''
    Breaks down the unstructured languages column into two columns: languages_used and language_sizes.
    The first is a list of the languages used in the repository and the second is the size of each language.
    '''
    def get_language_names(lang_data):
        '''
        Given a language data entry, it returns the names of the languages used in the repository.
        '''
        lang_data = ast.literal_eval(lang_data)
        # get the 'name' key's value from element in lang_0 
        names = [lang_data[i]['name'] for i in range(len(lang_data))]
        # convert to string
        names = ', '.join(names)
        return names

    def get_language_sizes(lang_data):
        '''
        Given a language data entry, it returns the sizes of the languages used in the repository.
        '''
        lang_data = ast.literal_eval(lang_data)
        # get the 'name' key's value from element in lang_0 
        sizes = [lang_data[i]['size'] for i in range(len(lang_data))]
        sizes = ', '.join([str(size) for size in sizes])
        return sizes

    # make a new column languages_used and language_sizes
    x_data['languagesUsed'] = x_data['languages'].apply(get_language_names)
    x_data['languagesSizes'] = x_data['languages'].apply(get_language_sizes)
    # drop the languages column
    x_data = x_data.drop('languages', axis=1)
    return x_data



def get_date_features(x_data_d, date_col, merge=False):
    '''
    This looks for the 'createdAt' column and breaks it into hour, day_of_week, day_of_year, month, quarter and year
    in a new dataframe.
    '''
    col = pd.to_datetime(x_data_d[date_col])
    # make a new pandas dataframe
    cols = pd.DataFrame()
    cols['hour'] = col.dt.hour
    cols['day_of_week'] = col.dt.dayofweek
    cols['day_of_year'] = col.dt.dayofyear
    cols['month'] = col.dt.month
    cols['quarter'] = col.dt.quarter
    cols['year'] = col.dt.year
    
    if merge:
        x_data_d = pd.concat([x_data_d, cols], axis=1)
        return x_data_d
    
    return cols


def impute_outliers(x_data,imputation_method="median", n_imputations=1):
    '''
    Discards outliers from the dataset.
    '''
    # for each numerical column if the IQD condition is met
    x_data_o = x_data.copy()
    for feat in x_data_o.columns:
        if type(x_data_o.iloc[0, x_data_o.columns.get_loc(feat)]) in [np.float64, np.int64]:
            Q1, Q3 = x_data_o[feat].quantile(0.25), x_data_o[feat].quantile(0.75)
            iqr = Q3 - Q1
            # replace outliers with the median
            if imputation_method == "median":
              x_data_o.loc[x_data_o[feat] > Q3 + 3 * iqr, feat] = x_data_o[feat].median()
            elif imputation_method == "multiple":
              x_data_o.loc[x_data_o[feat] > Q3 + 3 * iqr, feat] = np.nan #remove outliers

    if imputation_method == "multiple":
        np.random.seed(42)
        seeds = np.random.randint(0, 10000, n_imputations)
        imputed_datasets = []
        for seed in seeds:
            # initialize the used methods
            imputer = IterativeImputer(estimator=SGDRegressor(),
                                    max_iter=10, 
                                    random_state=seed, 
                                    n_nearest_features=5)
            scaler = StandardScaler()
            # remove categorical columns
            x_data_o_temp = x_data_o.select_dtypes(include=[np.float64, np.int64])
            columns = x_data_o_temp.columns
            # scale the data for numerical stability
            x_data_o_temp = pd.DataFrame(scaler.fit_transform(x_data_o_temp), columns=columns)
            # impute the outliers
            x_data_o_temp = pd.DataFrame(imputer.fit_transform(x_data_o_temp), columns=columns)
            # reverse the scaling
            x_data_o_temp = pd.DataFrame(scaler.inverse_transform(x_data_o_temp), columns=columns)
            # get back the categorical columns
            x_data_o_temp = pd.concat([x_data.select_dtypes(exclude=[np.float64, np.int64]), x_data_o_temp], axis=1)
            imputed_datasets.append(x_data_o_temp)

        if (len(imputed_datasets)==1):
            return imputed_datasets[0]
        else:
            return imputed_datasets

    return x_data_o

def impute_missing(x_data):
    x_data = x_data.replace(-1, 0)
    return x_data