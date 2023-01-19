# Import all packages we will use in this project
import pandas as pd
import numpy as np
import hashlib

import warnings
warnings.filterwarnings('ignore')

# Read in the Excel that has the transactions
df = pd.read_excel('bank.xlsx',sheet_name=0)

# Remove apostrophe at the end of the account number
df['Account No'] = df['Account No'].str[:-1].astype(int)

# Conver all NaN values to 0
df['WITHDRAWAL AMT'] = df['WITHDRAWAL AMT'].fillna(0)
df['DEPOSIT AMT'] = df['DEPOSIT AMT'].fillna(0)
df['CHQ.NO.'] = df['CHQ.NO.'].fillna(0)

df_Hash = df

# Create column that has all the details of the other columns as a string
df_Hash['Data'] = str(df_Hash[['DATE','TRANSACTION DETAILS','CHQ.NO.','VALUE DATE','WITHDRAWAL AMT','DEPOSIT AMT','BALANCE AMT']]).encode()
df_Hash['Data'] = df_Hash['Data'].astype(str)

df_Hash['Data'] = df_Hash.groupby(['Account No'])['Data'].transform(lambda x: ', '.join(x))

# Group all the data that has the same account number
df_Hash = df_Hash.groupby('Account No').first().reset_index()

#Only use in account number and transaction data field
df_Hash = df_Hash[['Account No','Data']]

# Convert account number to integer
df_Hash['Account No'] = df_Hash['Account No'].astype(int)

def hash_transaction(transaction):
    
    # Encode the transaction data as a string
    transaction_str = str(transaction).encode()

    # Create a hash object and use it to generate a hash of the transaction data
    hash_object = hashlib.sha256()
    hash_object.update(transaction_str)
    transaction_hash = hash_object.hexdigest()

    return transaction_hash

# Apply hash function to data column
df_Hash['Data'] = df_Hash['Data'].apply(hash_transaction)

