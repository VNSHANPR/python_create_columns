#df is the original dataframe with columns of type float which needs to be converted to Int64 in a single go
df1=df.dtypes  # Capture the types of the existing columns
a={} 
a=df1.to_dict()   # make a dictionary of column types

for k,v in enumerate(a):
    if a[v] == 'float64':
        print(k)  # k here is the Index of the matching "float64" column
        df[df.columns[k]]=df[df.columns[k]].astype('Int64')
