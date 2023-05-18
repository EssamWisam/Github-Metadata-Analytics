from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import re

backend_frameworks = [
    'django','ruby', 'node','laravel', 'flask', 
    'spring','express', 'asp', 'symfony', 'sinatra', 
    'phoenix', 'fastapi', 'koa', 'nestjs', 
    'mojolicious', 'sails', 'hapi', 'play framework', 'pyramid', 
    'cakephp', 'codeigniter', 'yii', 'fuelpHP', 'slim', 
    'rocket', 'falcon', 'adonis', 'loopback', 'strapi', 
    'feathers', 'restify', 'tornado', 'bottle', 'cherrypy', 
    'pycnic', 'tastypie', 'turbogears', 'zope', 'grails', 
    'micronaut', 'quarkus', 'ratpack', 'vert', 'scalatra', 
    'lagom', 'akka', 'javalin', 'vaadin', 'dropwizard'
]

frontend_frameworks = ['angular', 'react', 'vue','ember','backbone', 'polymer', 'svelte', 'meteor', 'aurelia', 'knockout']
sql_databases = ['mysql', 'postgresql', 'oracle', 'microsoft sql server', 'mssql', 'sqlite', 'mariadb']
nosql_databases = ['mongo', 'cassandra', 'redis', 'elasticsearch', 'couchbase', 'dynamodb', 'hbase', 'neo4j', 'firebase', 'couchdb', 'influxdb', 'arangodb', 'cockroachdb']
   

def generate_regex(lst):
    '''
    This function takes a list of strings and returns a list of regexes that match the strings in the list. but must be preceded by a non-word character.
    '''
    regexs = []
    for item in lst:
        regex = re.compile(r'(?<!\w)' + item)
        regexs.append(regex)
    return regexs

# generate regex for each framework
backend_frameworks_regex  = generate_regex(backend_frameworks)
frontend_frameworks_regex = generate_regex(frontend_frameworks)
sql_databases_regex       = generate_regex(sql_databases)
nosql_databases_regex     = generate_regex(nosql_databases)


def handle_synonyms(arr, synonyms):
            '''
            This function takes an array and a list of synonyms and returns the array with the synonyms replaced with the first element in the list.
            '''
            pivot = synonyms[0]

            for i in range(len(arr)):
                if arr[i] in synonyms:
                    arr[i] = pivot
        
            # remove duplicates
            return list(set(arr))


def parse_description(description):
        '''
        This function takes a description and returns a dictionary that contains the frameworks used in the description.
        '''
        description = description.lower()
        description = description.replace('\n', ' ')
        
        front_end = []
        back_end = []
        no_sql = []
        sql = []

        for i, regex in enumerate(frontend_frameworks_regex):
            if regex.search(description):
                front_end.append(frontend_frameworks[i])

        for i, regex in enumerate(backend_frameworks_regex):
            if regex.search(description):
                back_end.append(backend_frameworks[i])
        
        for i, regex in enumerate(nosql_databases_regex):
            if regex.search(description):
                no_sql.append(nosql_databases[i])

        for i, regex in enumerate(sql_databases_regex):
            if regex.search(description):
                sql.append(sql_databases[i])


        sql = handle_synonyms(sql, ['mssql', 'microsoft sql server'])

        back_end = handle_synonyms(back_end, ['express', 'node'])

        return {
            'front_end': front_end,
            'back_end': back_end,
            'no_sql': no_sql,
            'sql': sql
        }

def extend_dataset_with_frameworks(ds):
    '''
    This function takes a dataset and extends it with the frameworks used in the description of each job.
    '''
 
    ds = ds.copy()

    back_ends = []
    front_ends = []
    no_sqls = []
    sqls = []

    rows_to_be_removed = []

    for i in range(len(ds)):
        res = parse_description(ds.iloc[i]['description'])
        if res['back_end'] == [] and res['front_end'] == [] and res['no_sql'] == [] and res['sql'] == []:
            rows_to_be_removed.append(i)
            continue

        back_ends.append(res['back_end'])
        front_ends.append(res['front_end'])
        no_sqls.append(res['no_sql'])
        sqls.append(res['sql'])

    ds = ds.drop(rows_to_be_removed)

    ds['back_end'] = back_ends
    ds['front_end'] = front_ends
    ds['no_sql'] = no_sqls
    ds['sql'] = sqls

    return ds


# get the top 3 frequent back-end frameworks
def get_top_k_from_technology(ds, tech, k):
    '''
    This function takes a dataset and a technology and returns the top k most frequent frameworks used in the dataset.
    '''
    tech_freq = Counter(t for row in ds[tech] for t in row)
    top_k = [t for t, count in tech_freq.most_common(k)]
    return top_k
    


def get_front_ends_for_top_3_back_ends(ds):

    '''
    This function takes a dataset and returns a dictionary that maps each back end framework to its front end frameworks.
    '''

    top_3_backend = get_top_k_from_technology(ds,'back_end', k=3)
    
    # create a dictionary that maps each back end framework to its front end frameworks and intialize it with the top 3 back end frameworks
    back_to_front = {}
    for backend in top_3_backend:
        back_to_front[backend] = []

    for i in range(len(ds)):
        for backend in ds.iloc[i]['back_end']:
            if backend in back_to_front:
                back_to_front[backend] += ds.iloc[i]['front_end']

    # couting the frequency of each front end framework
    def count_freq(lst):
        freq = {}
        for item in lst:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        return freq
    
    for back_end in back_to_front:
        back_to_front[back_end] = {k: v for k, v in sorted(count_freq(back_to_front[back_end]).items(), key=lambda item: item[1], reverse=True)}


    return back_to_front 



def show_backend_databases_heatmap(ds):

    '''
    This function takes a dataset and shows a heatmap of the back end frameworks and the databases used with them.
    '''

    # get the top 5 frequent back-end frameworks
    backends = get_top_k_from_technology(ds,'back_end',5)
    sqls     = get_top_k_from_technology(ds,'sql',5)
    nosqls   = get_top_k_from_technology(ds,'no_sql',5)

    sqls_counts = []
    nosqls_counts = []

    for sql in sqls:
        for backend in backends:
            sqls_counts.append(len(ds[ (ds['back_end'].apply(lambda x: backend in x)) & (ds['sql'].apply(lambda x: sql in x)) ]))        

    for nosql in nosqls:
        for backend in backends:
            nosqls_counts.append(len(ds[ (ds['back_end'].apply(lambda x: backend in x)) & (ds['no_sql'].apply(lambda x: nosql in x)) ]))

    # Create a numpy array of the frequency counts
    sqls_counts = np.array(sqls_counts).reshape(5,5)
    nosqls_counts = np.array(nosqls_counts).reshape(5,5)

    # Create the heatmap using seaborn
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(sqls_counts, annot=True, fmt='d', cmap='Blues', xticklabels=backends, yticklabels=sqls)
    # Set the title and axis labels
    ax.set_title('Frequency of occurrence for sql and back-end frameworks')
    ax.set_xlabel('Back-end frameworks')
    ax.set_ylabel('Sql databases')


    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(nosqls_counts, annot=True, fmt='d', cmap='Blues', xticklabels=backends, yticklabels=nosqls)
    # Set the title and axis labels
    ax.set_title('Frequency of occurrence for no-sql and back-end frameworks')
    ax.set_xlabel('Back-end frameworks')
    ax.set_ylabel('No-sql databases')
    plt.style.use('dark_background')
    # Show the plot
    plt.show()



def explore_technology(ds, technology, title, top_n):

    '''
    This function takes a dataset, a technology, a title and the number of top frameworks to show and shows a pie chart of the top frameworks used in the dataset.
    '''

    tech = []
    for i in ds[technology]:
        tech.extend(i)
    tech = list(tech)

    labels = set(tech)
    sizes = [tech.count(i) for i in labels]
    labels, sizes = zip(*sorted(zip(labels, sizes), key=lambda x: x[1], reverse=True))

    plt.title(title)
    plt.pie(sizes[:top_n], labels = labels[:top_n], autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.style.use('dark_background')
    plt.show()


def show_histogram(data):

    '''
    This function takes a dictionary of data and shows a histogram of the data.
    '''

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    def plot_single_figure(title, labels, counts, ax):
        ax.set_facecolor('black')  # set background color to black
        ax.bar(labels, counts)  # set bar color to blue
        ax.set_title(title)
        ax.set_xticklabels(labels, rotation=90, color='white')
        ax.tick_params(axis='y', colors='white')  # set y-axis label color to white

    for i, title in enumerate(data.keys()):
        labels = list(data[title].keys())
        counts = list(data[title].values())
        plot_single_figure(title, labels, counts, axs[i])

    plt.style.use('dark_background')
    plt.tight_layout()
    plt.show()



    