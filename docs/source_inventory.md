# Source Inventory

## 1. Customers Data
**Source name:** customers.csv  
**Source-system type:** Local flat file  
**Data format:** CSV  
**Structured / semi-structured / unstructured:** Structured  
**Expected update pattern:** Periodic updates  
**Likely acquisition method:** File read via pandas.read_csv  
**Schema location or schema owner:** Inferred from file header  
**Possible primary/business key:** customer_id  
**Potential schema-evolution risk:** Low  
**Potential data-quality risk:** Missing fields and inconsistent text formatting.

## 2. Orders Data
**Source name:** orders.json  
**Source-system type:** Exported NoSQL document  
**Data format:** JSON  
**Structured / semi-structured / unstructured:** Semi-structured  
**Expected update pattern:** Continuous  
**Likely acquisition method:** File read via pandas.read_json  
**Schema location or schema owner:** Embedded in file / E-commerce App Team  
**Possible primary/business key:** order_id  
**Potential schema-evolution risk:** High  
**Potential data-quality risk:** Null values and inconsistent timestamp formatting.  

## 3. Products Data
**Source name:** products.parquet  
**Source-system type:** Columnar storage file  
**Data format:** Parquet  
**Structured / semi-structured / unstructured:** Structured  
**Expected update pattern:** Batch  
**Likely acquisition method:** File read via pandas.read_parquet  
**Schema location or schema owner:** Strictly embedded in Parquet metadata  
**Possible primary/business key:** product_id  
**Potential schema-evolution risk:** Low  
**Potential data-quality risk:** Negative prices/quantities.  

## 4. External Data
**Source name:** REST API Endpoint  
**Source-system type:** Web Service  
**Data format:** JSON (Typical for APIs)  
**Structured / semi-structured / unstructured:** Semi-structured  
**Expected update pattern:** Real-time  
**Likely acquisition method:** HTTP GET requests via requests library  
**Schema location or schema owner:** API Documentation / Third-party provider  
**Possible primary/business key:** Unique ID from the API response payload  
**Potential schema-evolution risk:** Medium  
**Potential data-quality risk:** Network timeouts and rate limiting.  