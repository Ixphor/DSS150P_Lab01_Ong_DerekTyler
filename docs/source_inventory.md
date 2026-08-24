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

## 5. PostgreSQL Source
**Table Name:** support_tickets  
**Constraints/Keys:** ticket_id is the Primary Key.  
**Row Count:** 250  

**Columns, Data Types, and Nullability:**
* ticket_id: integer (NOT NULL)
* customer_id: character varying (NOT NULL)
* category: character varying (NOT NULL)
* priority: character varying (NOT NULL)
* assigned_agent: character varying (Nullable)
* opened_at: timestamp without time zone (NOT NULL)
* resolved_at: timestamp without time zone (Nullable)
* status: character varying (NOT NULL)

**Five Sample Rows:**
| ticket_id | customer_id | category | priority | assigned_agent | opened_at | resolved_at | status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | C0246 | Technical | High | J. Reyes | 2026-06-19 04:00:00 | 2026-06-21 13:00:00 | Resolved |
| 2 | C0130 | Product | Medium | J. Reyes | 2026-05-26 07:00:00 | 2026-05-26 23:00:00 | Closed |
| 3 | C0094 | Delivery | Medium | J. Reyes | 2026-03-28 09:00:00 | 2026-03-31 17:00:00 | Closed |
| 4 | C0057 | Technical | High | L. Tan | 2026-04-25 19:00:00 | | In Progress |
| 5 | C0120 | Delivery | High | R. Cruz | 2026-01-20 02:00:00 | 2026-01-22 21:00:00 | Resolved |