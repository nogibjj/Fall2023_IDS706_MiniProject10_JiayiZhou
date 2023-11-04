## Fall2023_IDS706 Mini Project 10: PySpark Data Processing
### by Jiayi Zhou [![CI](https://github.com/nogibjj/Fall2023_IDS706_MiniProject10_JiayiZhou/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Fall2023_IDS706_MiniProject10_JiayiZhou/actions/workflows/cicd.yml)

### Purpose
This is for class data engineering mini project 10. It uses PySpark to perform data processing, including a Spark SQL query and one data transformation on a large dataset.


### Requirements
  * Use PySpark to perform data processing on a large dataset
  * Include at least one Spark SQL query and one data transformation

### Functionality
The code does data processing with Spark SQL and transformations:
  * [E] Extract a dataset from a URL with CSV format.
  * [T] Transform the data by filtering to get it ready for analysis.
  * [L] Load the transformed data into a database table using Spark SQL.
  * [Q] Accept and execute SQL queries on the database to analyze and retrieve insights from the data.

### Preparation:
1. open codespaces
2. wait for environment to be installed
3. run: `python main.py`
4. [Pyspark Output Data/Summary Markdown File](pyspark_output.md)

### Format code
1. Format code: `make format`
2. Lint code: `make lint`
3. Test code: `make test`


