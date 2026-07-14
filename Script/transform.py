import pandas as pd
def clean_reviews(df):

    df["review_comment_title"] = df["review_comment_title"].fillna("No Title")

    df["review_comment_message"] = df["review_comment_message"].fillna("No Comment")

    return df

def clean_products(df):

    df["product_category_name"] = df["product_category_name"].fillna("Unknown")

    numeric_columns = [
        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm"
    ]

    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].median())

    return df

def clean_orders(df):

    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for column in date_columns:
        df[column] = pd.to_datetime(df[column])

    return df

def transform_data(datasets):

    datasets["olist_order_reviews_dataset"] = clean_reviews(
        datasets["olist_order_reviews_dataset"]
    )

    datasets["olist_products_dataset"] = clean_products(
        datasets["olist_products_dataset"]
    )

    datasets["olist_orders_dataset"] = clean_orders(
        datasets["olist_orders_dataset"]
    )

    print("Transformation completed.")

    return datasets

