import pandas as pd
import mysql.connector
print("connector")
conn=mysql.connector.connect(host="localhost",user="****",password="*****",database="ETL")
cursor=conn.cursor()

def load_table(cursor, table_name, df):
    try:
        columns = ",".join(df.columns)

        placeholders = ",".join(["%s"] * len(df.columns))

        query = f"""
        INSERT INTO {table_name}
        ({columns})
        VALUES ({placeholders})
        """

        data = list(df.itertuples(index=False, name=None))

        cursor.executemany(query, data)

        print(f"{table_name} loaded successfully")

    except Exception as e:
        print(f"Error loading {table_name}: {e}")

carts=pd.read_parquet("carts_cleaned.parquet")
reviews=pd.read_parquet("reviews.parquet")
address=pd.read_parquet("address.parquet")
user=pd.read_parquet("users_cleaned.parquet")
products=pd.read_parquet("products_cleaned.parquet")
credentials=pd.read_parquet(r"C:\Users\SHASHANK\OneDrive\Desktop\Etl_pipeline\credentials.parquet")

load_table(cursor, "products", products)
load_table(cursor, "reviews", reviews)
load_table(cursor, "users", user)
load_table(cursor, "address", address)
load_table(cursor, "credentials", credentials)
load_table(cursor, "carts", carts)

conn.commit()

cursor.close()
conn.close()

print("Loading completed successfully")