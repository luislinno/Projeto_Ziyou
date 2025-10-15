# Import libs
import pandas as pd

def RemoveDuplicates(df, coluna):
    df_sem_duplicadas = df.drop_duplicates(subset=[coluna])
    return df_sem_duplicadas

# Leitura dos arquivos CSV

df_olist_orders_bronze = pd.read_csv('C:\\Users\\Nando\\Desktop\\Projeto_Ziyou\\Projeto_Ziyou\\data\\bronze\\olist_orders_dataset.csv')

df_olist_order_items_bronze = pd.read_csv('C:\\Users\\Nando\\Desktop\\Projeto_Ziyou\\Projeto_Ziyou\\data\\bronze\\olist_order_items_dataset.csv')

df_olist_products_bronze = pd.read_csv('C:\\Users\\Nando\\Desktop\\Projeto_Ziyou\\Projeto_Ziyou\\data\\bronze\\olist_products_dataset.csv')

# Validação da integridade das PKs e FKs

df_olist_orders_silver = RemoveDuplicates(df_olist_orders_bronze, 'order_id')

df_olist_order_items_silver = RemoveDuplicates(df_olist_order_items_bronze, 'order_id')

df_olist_products_silver = RemoveDuplicates(df_olist_products_bronze, 'product_id')

# Salvando os dados na camada Silver

df_olist_orders_silver.to_csv("C:\\Users\\Nando\\Desktop\\Projeto_Ziyou\\Projeto_Ziyou\\data\\silver\\olist_orders_silver.csv")

df_olist_order_items_silver.to_csv("C:\\Users\\Nando\\Desktop\\Projeto_Ziyou\\Projeto_Ziyou\\data\\silver\\olist_order_items_silver.csv")

df_olist_products_silver.to_csv("C:\\Users\\Nando\\Desktop\\Projeto_Ziyou\\Projeto_Ziyou\\data\\silver\\olist_products_silver.csv")



