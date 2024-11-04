from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Membuat SparkSession dengan koneksi ke Kafka
spark = SparkSession.builder \
    .appName("KafkaSparkStructuredStreaming") \
    .master("local[*]") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0") \
    .getOrCreate()

# Membaca stream data dari Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor-suhu") \
    .load()

# Mendefinisikan schema data
schema = StructType([
    StructField("sensor_id", StringType(), True),
    StructField("suhu", DoubleType(), True)
])

# Mengonversi value dari binary ke JSON
sensor_df = df.selectExpr("CAST(value AS STRING) as json") \
    .select(from_json(col("json"), schema).alias("data")) \
    .select("data.*")

# Memfilter suhu di atas 80°C
filtered_df = sensor_df.filter(col("suhu") > 80)

# Menulis output ke console
query = filtered_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
