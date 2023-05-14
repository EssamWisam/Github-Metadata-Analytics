### contains implementations for functions to be used (directly called) in the notebook

def get_transactions(df):
    transactions = df['languagesUsed'].tolist()
    transactions = [x.split(',') for x in transactions]
    return transactions