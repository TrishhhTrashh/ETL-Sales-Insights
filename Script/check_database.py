import duckdb

con = duckdb.connect("../database/olist.duckdb")

print("Tables:")
print(con.execute("SHOW TABLES").fetchall())

print("\nNumber of customers:")
print(con.execute("""
SELECT COUNT(*)
FROM olist_customers_dataset
""").fetchall())

print("\nFirst 5 customers:")
print(con.execute("""
SELECT *
FROM olist_customers_dataset
LIMIT 10
""").fetchdf())

con.close()