import pandas as pd


data = pd.read_csv('upload_fileupload.csv')

#Removing Duplicates and keeping last one
data = data.drop_duplicates(subset=['file_uploaded','name'], keep='last', inplace=True)
print(data)