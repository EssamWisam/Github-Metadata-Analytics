import matplotlib.pyplot as plt



def explore_license(x_data_d):
    '''
    Explore the licenses used in the dataset via a visual plot.
    '''
    # First, we get their number (and counts, max as may use later)
    license_nums =  len(x_data_d['license'].unique())
    license_dict = x_data_d['license'].value_counts().to_dict()
    max_count = max(license_dict.values())

    # Second we set up a plot with 6 columns and as much needed rows
    num_cols = 6
    num_rows = license_nums // num_cols + 1 
    plt.style.use('dark_background')
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(20, 20))

    # Make the plot more beautiful
    
    plt.rcParams['figure.dpi'] = 100
    
    # For each license
    for i, (license_name, count) in enumerate(license_dict.items()):
        row, col = i // num_cols, i % num_cols
        
        # split the license name into words
        license_name = license_name.split()
        
        # put a \n after every two words
        for i, word in enumerate(license_name):
            if i % 2 == 0 and i != 0:
                license_name[i] = '\n' + word
            if word == 'Microsoft':             # special case
                license_name[i] = word + '\n'
        license_name = ' '.join(license_name)
        
        # Replace -1 with None
        if license_name == '-1':
            license_name = 'None'
        
        # Set font size and family
        font_size = 15 if len(license_name) < 30 else 12 
        fontfamily = 'sans-serif'
        
        # Set box style and color
        bbox = dict(boxstyle="round",  pad=2, fc='teal', lw=2)
        
        # Set the text at the center of the grid cell
        axes[row, col].text(0.5, 0.5, license_name, horizontalalignment='center', verticalalignment='center', fontsize=font_size, bbox=bbox, c='white', fontfamily=fontfamily)
        axes[row, col].axis('off')
            
    # remove unused plots
    for i in range(license_nums, num_rows * num_cols):
        fig.delaxes(axes[i // num_cols, i % num_cols])

    axes[7, 1].text(3.5, 0.5, f"There are over ~{license_nums} licenses in the dataset", horizontalalignment='center', verticalalignment='center', fontsize=20, c='white', fontfamily='sans-serif')

    plt.show()
    

def fraction_of_license(x_data_d):
    '''
    Given a dataset of repos, find the fraction of repos with a license
    '''
    # Find the number and ratio of present licenses 
    num_present_license = x_data_d[x_data_d['license'] != '-1'].count()
    license_ratio = num_present_license[0]/ len(x_data_d)

    # Find the number and ratio of present codes of conduct where there's license
    num_present_codes_licenses = x_data_d[(x_data_d['codeOfConduct'] != '-1') & (x_data_d['license'] != '-1')].count()
    coc_license_ratio = num_present_codes_licenses[0] / len(x_data_d)

    # Find the number and ratio of present codes of conduct where there's no license
    num_present_codes_nolicense = x_data_d[(x_data_d['codeOfConduct'] != '-1') & (x_data_d['license'] == '-1')].count()
    coc_nolicense_ratio = num_present_codes_nolicense[0] / len(x_data_d)
    
    # Plot three pie charts; one for each ratio and let the labels be below the pie charts
    plt.rcParams['figure.dpi'] = 200
    plt.style.use('dark_background')
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Fraction of Repos with License and Code of Conduct', fontsize=16)
    ax1.pie([license_ratio, 1-license_ratio], labels=['License', 'No License'], autopct='%1.1f%%', shadow=True, startangle=90,  colors=['#ffff00','#D0D0D0'], textprops={'fontsize': 8, 'color': 'black'})
    ax1.set_title('License')
    ax2.pie([coc_license_ratio, 1-coc_license_ratio], labels=['Code of Conduct', 'No Code of Conduct'], autopct='%1.1f%%', shadow=True, startangle=90, colors=['#ffff00','#D0D0D0'], textprops={'fontsize': 8, 'color': 'black'})
    ax2.set_title('Code of Conduct with License')
    ax3.pie([coc_nolicense_ratio, 1-coc_nolicense_ratio], labels=['Code of Conduct', 'No Code of Conduct'], autopct='%1.1f%%', shadow=True, startangle=90, colors=['#ffff00','#D0D0D0'], textprops={'fontsize': 8, 'color': 'black'})
    ax3.set_title('Code of Conduct without License')
    plt.show()
    
    
    
    # Find the top 10 licenses and plot in a bar chart
def top_10_licenses(x_data_d):
    '''
    Given a dataset of repos, find the top 10 licenses and plot in a bar chart
    '''
    # Find the top 10 licenses
    top_10_licenses = x_data_d['license'].value_counts().head(12)    
    top_10_licenses.pop('-1')
    top_10_licenses.pop('Other')
    total_num_licenses = sum(top_10_licenses.values)
    # Plot the top 10 licenses in a bar chart
    plt.rcParams['figure.dpi'] = 200
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 5))
    # add counts to the bars
    for i, v in enumerate(top_10_licenses.values):
        ax.text(i-0.25, v+1.5, str(round(v/total_num_licenses,2)), color='white', fontweight='bold')
        
    fig.suptitle('Top 10 Licenses', fontsize=16)
    ax.bar(top_10_licenses.index, top_10_licenses.values, color='aqua')
    ax.set_xlabel('License')
    ax.set_ylabel('Number of Repos')
    plt.xticks(rotation=90)
    plt.show()