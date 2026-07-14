import duckdb
from pathlib import Path


def load_data(datasets):

    # Database file location
    db_path = Path("../database/olist.duckdb")

    # Create the database folder if it doesn't exist
    db_path.parent.mkdir(parents=True, exist_ok=True)

    # Connect to DuckDB (creates the database if it doesn't exist)
    con = duckdb.connect(str(db_path))

    # Load each DataFrame into DuckDB
    for table_name, df in datasets.items():

        con.execute(f"""
            CREATE OR REPLACE TABLE {table_name} AS
            SELECT * FROM df
        """)

        print(f"Loaded table: {table_name}")

    con.close()

    print("\nAll datasets have been loaded into DuckDB successfully!")