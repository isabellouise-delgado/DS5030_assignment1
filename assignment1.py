# %%
import pandas as pd
import numpy as np

def download_data(force=False):
    """Download and extract course data from Zenodo."""
    import urllib.request, zipfile, os
    
    zip_path = 'data.zip'
    data_dir = 'data'
    
    if not os.path.exists(zip_path) or force:
        print("Downloading course data")
        urllib.request.urlretrieve(
            'https://zenodo.org/records/16954427/files/data.zip?download=1',
            zip_path
        )
        print("Download complete")
    else:
        print("Download file already exists")
        
    if not os.path.exists(data_dir) or force:
        print("Extracting data files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
        print("Data extracted")
    else:
        print("Data directory already exists")

download_data()
# %%

df = pd.read_csv('data/ames_prices.csv')
# %%
price_na = df['price'].isna() #numeric variable
miscfeature_na = df['Misc.Feature'].isna() #categorical variable

np.sum(price_na)
np.sum(miscfeature_na)
# %%
df['price'].describe()
# %%
df['Misc.Feature'].value_counts()
# %%

# Questions: Does having specific features increase the price of the house? What types of features increase the price? 
# Stakeholders - real estate agents, property companies, potential home owners
# Ethics - price vs. affordabilty, are higher prices houses displacing previous owners