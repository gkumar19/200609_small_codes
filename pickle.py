import pandas as pd
import pickle

df = pd.DataFrame({'A':[1,2], 'B': [3,4]})
with open('pickle_file', 'wb') as f: #b stand for binary
    pickle.dump(df, f)
with open('pickle_file', 'rb') as f:
    df = pickle.load(f)
