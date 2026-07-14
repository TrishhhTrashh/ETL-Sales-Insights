import duckdb
from pathlib import Path

# Connect to DuckDB
con = duckdb.connect("../database/olist.duckdb")

# Create reports folder if it doesn't exist
reports_path = Path("../reports")
reports_path.mkdir(parents=True, exist_ok=True)

# Customers by State
query = """
SELECT customer_state,
       COUNT(*) AS total_customers
FROM olist_customers_dataset
GROUP BY customer_state
ORDER BY total_customers DESC;
"""

customers = con.execute(query).fetchdf()
customers.to_csv(reports_path / "customers_by_state.csv", index=False)

print("customers_by_state.csv created")


# Orders by Status

query = """
SELECT order_status,
       COUNT(*) AS total_orders
FROM olist_orders_dataset
GROUP BY order_status
ORDER BY total_orders DESC;
"""

orders = con.execute(query).fetchdf()
orders.to_csv(reports_path / "orders_by_status.csv", index=False)

print("orders_by_status.csv created")

# Payment Distribution

query = """
SELECT payment_type,
       COUNT(*) AS total_payments
FROM olist_order_payments_dataset
GROUP BY payment_type
ORDER BY total_payments DESC;
"""

payments = con.execute(query).fetchdf()
payments.to_csv(reports_path / "payment_distribution.csv", index=False)

print("payment_distribution.csv created")

#  Top Product Categories

query = """
SELECT
    p.product_category_name,
    COUNT(*) AS total_products
FROM olist_products_dataset p
GROUP BY p.product_category_name
ORDER BY total_products DESC
LIMIT 10;
"""

categories = con.execute(query).fetchdf()
categories.to_csv(reports_path / "top_categories.csv", index=False)

print("top_categories.csv created")

# Average Delivery Time
query = """
SELECT
    order_id,
    order_status,
    order_purchase_timestamp,
    order_delivered_customer_date,
    order_estimated_delivery_date,

    DATE_DIFF(
        'day',
        order_purchase_timestamp,
        order_delivered_customer_date
    ) AS delivery_days,

    DATE_DIFF(
        'day',
        order_delivered_customer_date,
        order_estimated_delivery_date
    ) AS days_before_estimated_delivery

FROM olist_orders_dataset

WHERE order_delivered_customer_date IS NOT NULL;
"""

delivery = con.execute(query).fetchdf()

delivery.to_csv(
    reports_path / "delivery_details.csv",
    index=False
)

print("delivery_time.csv created")

# Close connection
con.close()

print("\nAll reports generated successfully!")