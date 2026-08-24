# DSS150P_Lab01_Ong_DerekTyler

**Laboratory:** Laboratory 1  
**Name:** Derek Tyler Ong  
**Student Number:** 2022135297

## Purpose of this Lab
The purpose of this laboratory is to establish a robust, containerized data engineering workspace and perform initial data profiling. By interacting with multiple raw data formats, I cam identify data quality risks and establish basic data contracts to ensure reliable downstream pipeline development.

## Software Requirements
* Python 3.10+
* Docker Desktop & Docker Compose
* Git
* VSCode
* PostgreSQL Client Tools 

## Exact Steps to Reproduce the Environment
1. Clone this repository.
2. Open the repository folder in VS Code.
3. Open the terminal and create a virtual environment: python -m venv .venv
4. Activate the virtual environment: .\.venv\Scripts\activate
5. Install the required dependencies: pip install -r requirements.txt

## Exact Commands to Start and Stop PostgreSQL
* **Start PostgreSQL:** docker compose up -d
* **Stop PostgreSQL:** docker compose down

## How to Run Each Python Script
* **Verify Database Connection:** python src/verify_environment.py
* **Profile CSV, JSON, and Parquet Data:** python src/profile_sources.py
* **Ingest REST API Data:** python src/inspect_api.py

## Description of Each Source
* customers.csv: A flat file containing demographic customer data.
* orders.json: A semi-structured JSON file of e-commerce transactions containing a nested shipping object. 
* products.parquet: A highly structured, columnar storage file containing product inventory.
* REST API: A public JSON placeholder endpoint (https://jsonplaceholder.typicode.com/posts) yielding 100 dummy records.
* support_tickets: A relational PostgreSQL table containing 250 records of customer support interactions with strict data types.

## Known Limitations or Unresolved Questions
* The customers.csv file requires a deduplication step before it can safely enforce a primary key due to the 3 duplicate records.
* The orders.json file contains nested dictionaries that must be flattened to a tabular format before relational storage.
* The public REST API may change its payload structure without notice, since it is an external source.