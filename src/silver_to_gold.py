#Import libs
import pandas as pd

# Leitura dos arquivos CSV
df_olist_orders_silver = pd.read_csv("C:\\Users\\Nando\\Desktop\\Projeto_Ziyou\\Projeto_Ziyou\\data\\silver\\olist_orders_silver.csv")

df_olist_order_items_silver = pd.read_csv("C:\\Users\\Nando\\Desktop\\Projeto_Ziyou\\Projeto_Ziyou\\data\\silver\\olist_order_items_silver.csv")

df_olist_products_silver = pd.read_csv("C:\\Users\\Nando\\Desktop\\Projeto_Ziyou\\Projeto_Ziyou\\data\\silver\\olist_products_silver.csv")


# Agregando as bases a tabela gold
f_olist_order_stagin = pd.merge(df_olist_orders_silver, df_olist_order_items_silver, on='order_id', how='left')

f_olist_order_gold = pd.merge(f_olist_order_stagin, df_olist_products_silver, on='product_id', how='left')

# Salvando os dados agregados na camada gold
f_olist_order_gold.to_csv("C:\\Users\\Nando\\Desktop\\Projeto_Ziyou\\Projeto_Ziyou\\data\\gold\\olist_order_gold.csv")
