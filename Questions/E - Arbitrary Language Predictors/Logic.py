import matplotlib.pyplot as plt
import seaborn as sns


def language_splits(x_data_d):
    '''
    This function splits the data into 10 languages and returns a dictionary of the splits and a list of the top 10 languages.
    '''
    # replace all the '-1' values with 'Undetected'
    x_data_d["primaryLanguage"] = x_data_d["primaryLanguage"].replace('-1', 'Undetected')
    x_data_d = x_data_d[["stars", "defaultBranchCommitCount", "pullRequests", "primaryLanguage"]]

    top_langs = x_data_d["primaryLanguage"].value_counts().head(10).index.tolist()

    # Make a 10x3 grid of plots. So for each language we have a histogram number of commits, number of stars, number of pull requests
    splits = {}
    for lang in top_langs:
        splits[lang] = x_data_d[x_data_d["primaryLanguage"] == lang]
    
    return splits, top_langs


def density_plots(splits, top_langs):
    '''
    This function plots the distributions of the starts, commits and pull requests features for the 10 languages.
    '''
    # increase dpi
    plt.rcParams['figure.dpi'] = 300
    plt.style.use('dark_background')
    fig, axes = plt.subplots(1, 3, figsize=(25, 6))
    # Lets start with a plot that superimposes all of them

    # Choose 10 light colors for the 10 languages. should be really light
    colors = ["#00BFFF", "#00Ff9f", "#2FF2EE", "#FFD700", "#FF8C00", "#11f20f", "#FF00FF", "#FFFFFF", "#FF4500", "#FFDAB9"]

    for i, lang in enumerate(top_langs):
        # Make 3 KDE plots
        sns.kdeplot(splits[lang]["stars"], ax=axes[0], fill=False, color=colors[i])
        # remove top and right spines     
        sns.kdeplot(splits[lang]["defaultBranchCommitCount"], ax=axes[1], fill=False, color=colors[i])
        sns.kdeplot(splits[lang]["pullRequests"], ax=axes[2], fill=False, color=colors[i])
        axes[0].set_title("Language Stars")
        axes[1].set_title("Language Commits")
        axes[2].set_title("Language Pull Requests")
        # remove top and right spines
        axes[0].spines['right'].set_visible(False)
        axes[0].spines['top'].set_visible(False)
        axes[1].spines['right'].set_visible(False)
        axes[1].spines['top'].set_visible(False)
        axes[2].spines['right'].set_visible(False)
        axes[2].spines['top'].set_visible(False)

    # Add a horizontal legend at the bottom (center) of the plot
    # add some space
    fig.subplots_adjust(bottom=0.2)
    fig.legend(labels=top_langs, loc="lower center", ncol=10)
    plt.show()




def bar_plots(splits, top_langs):
    '''
    This function plots the means and standard deviations of the 3 features for each language in 6 bar charts arranged in 2 rows.
    '''
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))
    
    for i, feature in enumerate(['stars', 'defaultBranchCommitCount', 'pullRequests']):
        lang_means = [splits[lang][feature].mean() for lang in top_langs]
        lang_stds = [splits[lang][feature].std() for lang in top_langs]
        
        axes[0, i].bar(top_langs, lang_means, color="#2FF2EE", alpha=0.7)
        axes[0, i].set_xticklabels(top_langs, rotation=90)
        axes[0, i].spines['right'].set_visible(False)
        axes[0, i].spines['top'].set_visible(False)
        axes[0, i].set_title(f'Mean {feature.capitalize()}')
        
        axes[1, i].bar(top_langs, lang_stds, color="#FFDF00", alpha=0.7)
        axes[1, i].set_xticklabels(top_langs, rotation=90)
        axes[1, i].spines['right'].set_visible(False)
        axes[1, i].spines['top'].set_visible(False)
        axes[1, i].set_title(f'STD {feature.capitalize()}')
        
    fig.tight_layout()
    plt.show()

# Make a 3D scatter plot of the 3 columns for each language
# take a random sample of 30% of each language
def scatter_plots(splits, top_langs):
    '''
    This function makes 3 2D scatter plots for each two pairs of columns for each language.
    '''
    colors = ["#00BFFF", "#00Ff9f", "#2FF2EE", "#FFD700", "#FF8C00", "#11f20f", "#FF00FF", "#FFFFFF", "#FF4500", "#FFDAB9"]

    splits_s = {}
    for lang in top_langs:
        splits_s[lang] = splits[lang].sample(frac=0.1)

    # Make 3 2D scatter plots for each two pairs of columns
    plt.rcParams['figure.dpi'] = 300
    plt.style.use('dark_background')
    fig, axes = plt.subplots(1, 3, figsize=(25, 6))
    for i, lang in enumerate(top_langs):
        axes[0].scatter(splits_s[lang]["stars"], splits_s[lang]["defaultBranchCommitCount"], color=colors[i], s=4.9)
        axes[1].scatter(splits_s[lang]["stars"], splits_s[lang]["pullRequests"], color=colors[i], s=4.9)
        axes[2].scatter(splits_s[lang]["defaultBranchCommitCount"], splits_s[lang]["pullRequests"], color=colors[i], s=4.9)
        axes[0].set_title("Stars vs Commits")
        axes[1].set_title("Stars vs Pull Requests")
        axes[2].set_title("Commits vs Pull Requests")
        # remove top and right spines
        axes[0].spines['right'].set_visible(False)
        axes[0].spines['top'].set_visible(False)
        axes[1].spines['right'].set_visible(False)
        axes[1].spines['top'].set_visible(False)
        axes[2].spines['right'].set_visible(False)
        axes[2].spines['top'].set_visible(False)

    # Add a horizontal legend at the bottom (center) of the plot
    # add some space
    fig.subplots_adjust(bottom=0.2)
    fig.legend(labels=top_langs, loc="lower center", ncol=10)
    plt.show()

def hyp_test_result(μ1, μ2, p_value, t, α, one_sided=False):
    '''
    Reports the findings from a one-tailed or two-tailed t-test given H0, H1, p-value, t-statistic and α.
    '''
    
    if one_sided:
        p_value /= 2
        if t > 0:
            ineq_0, ineq_1 = "<", ">"
        else:
            ineq_0, ineq_1 = ">", "<"
    else:
        ineq_0, ineq_1 = "=", "!="
        
    if p_value < α:
        return(f"Accept:\n {μ1} - {μ2} {ineq_1} 0")
    else:  
        return(f"Cannot Reject: {μ1} - {μ2}  {ineq_0} 0")
    

def normality_test(splits, top_langs):
    '''
    Test if the mean of each feature for each language is normally distributed.
    '''
    mean_splits = { lang: { "stars": [], "defaultBranchCommitCount": [], "pullRequests": [] } for lang in top_langs }

    for lang in top_langs:
        for i in range(50):
            mean_splits[lang]["stars"].append(splits[lang]["stars"].sample(300).mean())
            mean_splits[lang]["defaultBranchCommitCount"].append(splits[lang]["defaultBranchCommitCount"].sample(100).mean())
            mean_splits[lang]["pullRequests"].append(splits[lang]["pullRequests"].sample(100).mean())

    # include only javascript, python and C++ in mean_splits_mod
    mod_langs = ["JavaScript", "Python", "C"]
    mean_splits_mod = { lang: mean_splits[lang] for lang in mod_langs }

    density_plots(mean_splits_mod, mod_langs)