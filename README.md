# 🚀 End-to-End ETL Pipeline using Python, DuckDB, SQL & Power BI

## 📖 Project Overview

This project demonstrates the implementation of a complete ETL (Extract, Transform, Load) pipeline using the Olist Brazilian E-commerce dataset.

The pipeline extracts raw data from multiple CSV files, transforms and cleans the data using Python and Pandas, loads the processed data into DuckDB, performs SQL-based analysis, and visualizes business insights using Power BI.

---

## 🎯 Objectives

- Extract data from multiple CSV files.
- Clean and preprocess raw datasets.
- Load processed data into DuckDB.
- Perform SQL analysis on the loaded data.
- Generate business reports.
- Build an interactive Power BI dashboard.

---

## 🛠️ Technologies Used

- Python
- Pandas
- DuckDB
- SQL
- Power BI
- Git & GitHub
- VS Code

---

## 📂 Dataset

**Dataset:** Olist Brazilian E-commerce Public Dataset

The dataset contains information about:

- Customers
- Orders
- Products
- Sellers
- Payments
- Reviews
- Geolocation

---

## 📁 Project Structure

```
ETL Project/
│
├── data/
│   └── raw/
│
├── database/
│   └── olist.duckdb
│
├── reports/
│
├── Script/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── analysis.py
│   └── main.py
│
├── dashboard.pbix
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 ETL Workflow

### 1. Extract

- Read multiple CSV files from the raw data directory.
- Store each dataset as a Pandas DataFrame.

### 2. Transform

- Handle missing values.
- Convert date columns to datetime format.
- Clean customer reviews and product information.
- Prepare the data for analysis.

### 3. Load

- Load transformed datasets into DuckDB.
- Create tables for SQL querying.

### 4. Analyze

SQL queries were used to generate reports including:

- Customers by State
- Orders by Status
- Payment Method Distribution
- Product Category Analysis
- Delivery Performance

### 5. Visualize

Power BI dashboard was created to visualize:

- Customer distribution across states
- Order status
- Payment methods
- Delivery insights

---

## 📊 Dashboard Features

The dashboard includes:

- Total Orders
- Average Delivery Days
- Customers by State
- Order Status Distribution
- Payment Method Distribution
- Delivery Performance

---

## ▶️ How to Run the Project

### Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Navigate to the project scripts

```bash
cd Script
```

### Run the ETL pipeline

```bash
py main.py
```

### Generate analysis reports

```bash
py analysis.py
```

---

## 📈 Sample SQL Query

```sql
SELECT
    customer_state,
    COUNT(*) AS total_customers
FROM olist_customers_dataset
GROUP BY customer_state
ORDER BY total_customers DESC;
```

---

## 📸 Dashboard Preview

<img width="1331" height="756" alt="image" src="https://github.com/user-attachments/assets/f37ce906-3a02-4f84-861c-878e593e931f" />


---

## 🔮 Future Improvements

- Automate pipeline scheduling using Apache Airflow.
- Store data in PostgreSQL.
- Integrate cloud storage (AWS S3).
- Add logging and automated data validation.
- Build a real-time ETL pipeline.

---

## 👩‍💻 Author

**Trisha Maurya**

Bachelor of Technology (Computer Science with AI & ML)
