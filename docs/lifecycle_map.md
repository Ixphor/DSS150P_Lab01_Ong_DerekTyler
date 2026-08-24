# Data Lifecycle Map

## Lifecycle Table

| Lifecycle Element | What It Means | Example in This Lab | Primary Tool/Artifact | Possible Failure |
| :--- | :--- | :--- | :--- | :--- |
| **Source system** | The origin where raw data is generated before collection. | The provided CSV and the REST API endpoint. | Source files, External servers | The API endpoint might go offline. |
| **Ingestion/acquisition** | The process of extracting or downloading data from the source. | Reading the CSV files into memory or fetching data via API requests. | pandas and requests libraries | Network connection cuts during an API call. |
| **Storage** | The location where the ingested and processed data is saved. | The database which stores the structured outputs. | PostgreSQL container | The database container crashes or the storage disk runs out of space. |
| **Processing/transformation** | Cleaning and merging the raw data into a usable state. | Converting data types, handling missing values or normalizing structures. | pandas library | Memory overloads from large files. |
| **Data quality/validation** | Checking the data against rules to ensure accuracy and reliability. | Checking for null and missing values, ensuring unique primary keys, and validating API response codes. | pandas library | Corrupted rows bypass checks and API returns OK but is actually empty. |
| **Delivery** | Making the processed data accessible and available to users. | Loading the final cleaned dataframes into PostgreSQL tables. | SQLAlchemy and psycopg2-binary | Database authentication fails. |
| **Consumer** | The end-user that utilizes the finalized data for decision-making. | A user querying the database to build predictive models or generate reports. | Jupyter Notebooks or BI Tools | Human error if the user misinterprets the schema. |

<br>

## Data Flow Diagram

```mermaid
flowchart LR
    %% Define Sources
    subgraph Sources [Raw Data Sources]
        direction TB
        CSV[CSV source]
        JSON[JSON source]
        PRQ[Parquet source]
        API[REST API]
        PG_SRC[(PostgreSQL)]
    end

    %% Define Processing and Destination
    PIPE[Pipeline/Process]
    DEST[(Storage/Destination)]
    USER([Downstream Analyst or Application Customer])

    %% Map the flow
    CSV --> PIPE
    JSON --> PIPE
    PRQ --> PIPE
    API --> PIPE
    PG_SRC --> PIPE
    
    PIPE --> DEST
    DEST --> USER
    