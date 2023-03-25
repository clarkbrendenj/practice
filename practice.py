import pandas as pd
import matplotlib as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.min_rows', 7)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 300)
pd.set_option("max_colwidth", 40)
pd.reset_option("large_repr")
pd.set_option("expand_frame_repr", True)


df = pd.read_csv('./data/budget.csv', index_col=False)
print(df.head())
