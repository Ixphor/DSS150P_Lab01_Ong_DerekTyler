DROP SCHEMA IF EXISTS lab;

CREATE SCHEMA IF NOT EXISTS lab;

DROP TABLE IF EXISTS lab.customers;

CREATE TABLE lab.customers (
    customer_id TEXT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    -- Email and city are nullable because it was found before that there were 3 and 2 missing values respectively
    email TEXT,
    city TEXT,
    signup_date DATE NOT NULL,
    customer_segment TEXT NOT NULL,
    
    -- No primary key because:
    -- A PRIMARY KEY constraint is omitted because raw data profiling revealed 
    -- duplicate records (247 unique IDs out of 250 rows). Enforcing uniqueness 
    -- here would cause the initial raw data ingestion to fail. 
    
    CONSTRAINT chk_customer_id_format CHECK (customer_id SIMILAR TO 'C[0-9]%')
);