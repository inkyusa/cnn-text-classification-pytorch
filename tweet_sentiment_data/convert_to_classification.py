import pandas as pd

good_train_df =  pd.read_csv("./good_train.csv")
good_train_df['text'] = good_train_df['text'].astype(str)
good_train_df['text'].to_csv('good_train.pos', header=None,index=False)

bad_train_df =  pd.read_csv("./bad_train.csv")
bad_train_df['text'] = bad_train_df['text'].astype(str)
bad_train_df['text'].to_csv('bad_train.neg', header=None,index=False)

