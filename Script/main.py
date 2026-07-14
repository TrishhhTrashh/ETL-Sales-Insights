from extract import extract_data
from transform import transform_data
from load import load_data


def main():

    print("=" * 40)
    print("Starting ETL Pipeline")
    print("=" * 40)

    datasets = extract_data()

    datasets = transform_data(datasets)

    load_data(datasets)

    print("=" * 40)
    print("ETL Pipeline Completed Successfully!")
    print("=" * 40)


if __name__ == "__main__":
    main()
    