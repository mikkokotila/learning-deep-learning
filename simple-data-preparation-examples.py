import pandas as pd
import numpy as np

# FIRST ATTEMPT - get familiar with the dataset

# STEP 1 - load the data to memory
dataset = pd.read_msgpack('https://github.com/autonomio/datasets/raw/master/autonomio-datasets/parties_and_employment')

# STEP2 - clean the garbage (in this case wrong decimal point)
dataset.unemployment = dataset.unemployment.str.replace(',','.').astype(float)

# STEP 3 - convert the data in to a numpy array and remove extra columns
dataset = np.array(dataset)[0:,1:11]

# SECOND ATTEMPT - try something that makes sense and is easy to understand 

df = pd.read_msgpack('https://github.com/autonomio/datasets/raw/master/autonomio-datasets/parties_and_employment')

l = []
c = len(df) - 1
for i in range(c):
    temp = df.SDP[i+1] - df.SDP[i]
    l.append(temp > 0)

new_df = df.unemployment.str.replace(',','.').astype(float)
new_df = pd.DataFrame(new_df)
new_df = new_df[1:108]
new_df['sdp'] = l 
