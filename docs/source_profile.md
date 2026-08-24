# Source Data Profile Interpretations

## 1. customers.csv
* The raw file contains 2 fully duplicated rows, as well as missing values in the email and city columns. The downstream pipeline must include a deduplication step and an explicit null-handling strategy before this data is loaded into a relational database.
* The customer_id field has 247 distinct values across 250 rows. Once the duplicates are removed, this field is the candidate for the primary key.

## 2. orders.json
* The shipping column contains nested dictionary objects. A data flattening transformation will be required in the processing pipeline to unpack these dictionaries into standard relational columns.
* The order_timestamp column is initially ingested as a string object. The pipeline must explicitly cast this column to a standard datetime format to allow for accurate time-series analysis and database compatibility.
* There are no duplicate rows and zero null values in this file, with order_id possessing exactly 250 unique values. This is a highly reliable primary key.

## 3. products.parquet
* True to the columnar Parquet format, this dataset demonstrates excellent data quality. It contains zero null values and zero fully duplicated rows, meaning it will require minimal defensive cleaning compared to the CSV and JSON sources.
* The product_id field is perfectly unique and is fully ready to act as the primary key for downstream joins with the orders table.