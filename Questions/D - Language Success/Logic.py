import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#plt.rcParams['figure.dpi'] = 100
plt.style.use('dark_background')

def remove_2023(x_data_d):
  x_data_n = x_data_d[x_data_d['createdAt'].dt.year < 2023]
  return x_data_n


def outliers_pie_plot(x_data_d):
  """
  Plots a pie chart of the outliers in stars.

  """

  stars = x_data_d['stars']
  Q1, Q3 = stars.quantile(0.25), stars.quantile(0.75)
  iqr = Q3 - Q1
  outlier_ratio = sum(stars > Q3 + 1.5 * iqr) / len(stars)
  outlier_ratio += sum(stars < Q1 - 1.5 * iqr) / len(stars)

  # Create figure and axes objects
  fig, ax = plt.subplots(figsize=(2, 2))

  # Plot pie chart
  ax.pie([1 - outlier_ratio, outlier_ratio], labels=['Inlier', 'Outlier'], autopct='%1.1f%%', shadow=True,
          textprops={'color': 'black'})  # Set text color to black

  # Set title
  ax.set_title('Outliers in Stars')

  plt.show()

def remove_outliers(x_data, col):
  '''
    Removes outliers from the given column
  '''
  q1 = x_data[col].quantile(0.25)
  q3 = x_data[col].quantile(0.75)
  iqr = q3 - q1
  x_data = x_data[x_data[col] < q3 + 1.5 * iqr]
  x_data = x_data[x_data[col] > q1 - 1.5 * iqr]
  return x_data

def replace_missing_with_document(x_data_d):
  return x_data_d.replace({'primaryLanguage': {'-1': 'Document'}})

def remove_documents(x_data_d):
  return x_data_d[x_data_d['primaryLanguage'] != 'Document']

def stars_per_languages(x_data_d, num_top=10):
  """
  Plots the top 10 languages by stars.

  Args:
    x_data_d: The DataFrame containing the data.
    num_top: The number of top languages to plot.
  """

  top_languages = x_data_d.groupby('primaryLanguage')['stars'].sum().sort_values(ascending=False).head(num_top)
  top_languages_o = remove_outliers(x_data_d,'stars').groupby('primaryLanguage')['stars'].sum().sort_values(ascending=False).head(num_top)
  # choose a colormap and select a subset of colors
  colors=['#FDFD96']*5

  # plot 2 histogram with colored bars
  fig, (ax,bx) = plt.subplots(ncols=2, figsize=(15, 6))
  ax.bar(top_languages.index, top_languages.values, color=colors)
  bx.bar(top_languages_o.index, top_languages_o.values, color=colors)
  # add axis labels and title
  ax.set_xlabel('Language')
  ax.set_ylabel('Stars')
  ax.set_title('Top 10 Languages')
  bx.set_xlabel('Language')
  bx.set_ylabel('Stars')
  bx.set_title('Top 10 Languages (without outliers)')
  # rotate X axis labelsperry the platypus from phineas and ferb
  ax.set_xticklabels(top_languages.index, rotation=45)
  bx.set_xticklabels(top_languages_o.index, rotation=45)
  # adjust spacing between subplots
  plt.subplots_adjust(wspace=0.5)

  plt.show()


def yearly_stars_distribution_per_language(x_data_d):
  """
  Plots the yearly stars distribution for the top 5 languages.

  Args:
    x_data_d: The DataFrame containing the data.
  """
  x_data_d = remove_outliers(x_data_d)
  x_data_d['year'] = x_data_d['createdAt'].dt.year
  top_5_languages = x_data_d.groupby('primaryLanguage')['stars'].sum().sort_values(ascending=False).head(5).index
  filtered_df = x_data_d[x_data_d['primaryLanguage'].isin(top_5_languages)]

  fig, ax = plt.subplots(figsize=(15, 6))
  sns.boxplot(x='year', y='stars', hue='primaryLanguage', data=filtered_df, showfliers=False)
  ax.set_title('Yearly Stars Distribution for Top 5 Languages')
  ax.set_xlabel('Year')
  ax.set_ylabel('Stars')
  plt.show()