"""
library functions
"""
import os
import requests
from pyspark.sql import SparkSession

from pyspark.sql.types import (
     StructType, 
     StructField, 
     IntegerType, 
     StringType, 
     DoubleType
)

LOG_FILE = "pyspark_output.md"


def log_output(operation, output, query=None):
    """adds to a markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"The operation is {operation}\n\n")
        if query: 
            file.write(f"The query is {query}\n\n")
        file.write("The truncated output is: \n\n")
        file.write(output)
        file.write("\n\n")

def start_spark(appName):
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark

def end_spark(spark):
    spark.stop()
    return "stopped spark session"

def extract(
    url="""
   https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv?raw=true 
    """,
    file_path="data/Goose.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
 

    return file_path

def load_data(spark, data="data/Goose.csv", name="CompetitionRecord"):
    """load data"""
    # data preprocessing by setting schema
    schema = StructType([
        StructField("name", StringType(), True),
        StructField("year", IntegerType(), True),
        StructField("team", StringType(), True),
        StructField("league", StringType(), True),
        StructField("goose_eggs", IntegerType(), True),
        StructField("broken_eggs", IntegerType(), True),
        StructField("mehs", IntegerType(), True),
        StructField("league_average_gpct", DoubleType(), True),
        StructField("ppf", DoubleType(), True),
        StructField("replacement_gpct", DoubleType(), True),
        StructField("gwar", DoubleType(), True),
        StructField("key_retro", StringType(), True),
    ])

    df = spark.read.option("header", "true").schema(schema).csv(data)

    log_output("load data", df.limit(10).toPandas().to_markdown())

    return df


def query(spark, df, query, name): 
    """queries using spark sql"""
    df = df.createOrReplaceTempView(name)

    log_output("query data", spark.sql(query).toPandas().to_markdown(), query)

    return spark.sql(query).show()

def describe(df):
    summary_stats_str = df.describe().toPandas().to_markdown()
    log_output("describe data", summary_stats_str)

    return df.describe().show()

def example_transform(df):
    """does an example transformation on a predefiend dataset"""

    specific_year = 1921

    df = df.where(df.year == specific_year)

    log_output("transform data", df.limit(10).toPandas().to_markdown())

    return df.show()