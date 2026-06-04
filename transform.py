import pandas as pd
products_data=pd.read_parquet(r"C:\Users\SHASHANK\OneDrive\Desktop\Etl_pipeline\products.parquet")
users_data=pd.read_parquet(r"C:\Users\SHASHANK\OneDrive\Desktop\Etl_pipeline\users.parquet")
carts_data=pd.read_parquet(r"C:\Users\SHASHANK\OneDrive\Desktop\Etl_pipeline\carts.parquet")
df=pd.DataFrame(products_data)
df_carts=pd.DataFrame(carts_data)
df_users=pd.DataFrame(users_data)


df["brand"].fillna("Unknown", inplace=True)

df_product=df[["id","title","brand","description","category","price","rating","stock","sku","returnPolicy"]]


df_reviews=df[["id","reviews","rating"]]
df_reviews.rename(columns={"rating":"product_rating"},inplace=True)
df_reviews=df_reviews.explode("reviews")
df_reviews_base=pd.json_normalize(df_reviews["reviews"])
df_reviews=pd.concat([df_reviews[["id","product_rating"]].reset_index(drop=True),df_reviews_base.reset_index(drop=True)],axis=1)



df_user=df_users[["id","firstName","lastName","age","gender","email","phone"]]
print(df_users.columns)
df_credentials=df_users[["id","username","password","ip"]]
df_users.rename(
    columns={
        col: col.replace("address.", "")
        for col in df_users.columns
        if col.startswith("address.")
    },
    inplace=True
)
df_address=df_users[["id","address","country","city","state","postalCode"]]


print(df_carts.columns)
df_carts=df_carts.explode("products")
df_carts_normalized=pd.json_normalize(df_carts["products"])
df_carts_normalized.rename(
    columns={
        "id": "product_id",
        "title": "product_title",
        "price": "product_price",
        "quantity": "product_quantity",
        "total": "product_total",
        "discountedTotal": "product_discounted_total"
    },
    inplace=True
)
df_carts=pd.concat([df_carts.reset_index(drop=True),df_carts_normalized.reset_index(drop=True)],axis=1)
print(df_carts.columns)

df_address.to_parquet("address.parquet")
df_carts.to_parquet("carts_cleaned.parquet")
df_user.to_parquet("users_cleaned.parquet")
df_credentials.to_parquet("credentials.parquet")
df_product.to_parquet("products_cleaned.parquet")
df_reviews.to_parquet("reviews.parquet")