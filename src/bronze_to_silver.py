import pandas as pd

def CheckNull(df):
    

# Leitura do arquivo CSV

df = pd.read_csv('C:\\Users\\Nando\\Desktop\\Projeto_Ziyou\\Projeto_Ziyou\\data\\bronze\\olist_products_dataset.csv')

duplicated = df.duplicated()
print(duplicated.filter(like='False'))
