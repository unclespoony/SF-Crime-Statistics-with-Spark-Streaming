# SF-Crime-Statistics-with-Spark-Streaming

## Runing project in Udacity workspace environment

>**Step 1:**
>
>Open new console and run ./start.sh

>**Step 2:**
>
>Open new console and run /usr/bin/zookeeper-server-start config/zookeeper.properties

>**Step 3:**
>
>Open new console and run python kafka_server.py 

>**Step 4:**
>
>Open new console and run /usr/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sf.police.callsforsvc --from-beginning

>**Step 5:**
>
>Open new console and run spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py


## Project Questions:

>**Question 1:** How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
>
>**Answer:** Modifying the "maxOffsetsPerTrigger" property affects latency and throughput.  For example, I started with maxOffsetsPerTrigger = 200 and the progress report showed the following:
>
![Alt text](maxOffsetsResult1.png?raw=true "Optional Title")

>After changing maxOffsetsPerTrigger to 1000, the progress report showed:
>
![Alt text](maxOffsetsResult2.png?raw=true "Optional Title")
>
>Therefore while the number of records processed went up, the time to process also increased.


>**Question 2** What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
>
>**Answer:**
>I attempted multiple combinations of maxOffsetsPerTrigger and spark.default.parallelism, such as:
>maxOffsetsPerTrigger = 200 and spark.default.parallelism = 100
>maxOffsetsPerTrigger = 1000 and spark.default.parallelism = 100
>maxOffsetsPerTrigger = 800 and spark.default.parallelism = 200
>maxOffsetsPerTrigger = 800 and spark.default.parallelism = 300
>maxOffsetsPerTrigger = 500 and spark.default.parallelism = 200
>maxOffsetsPerTrigger = 750 and spark.default.parallelism = 200
>
>It seemed that having the spark.default.parallelism = 200 gave the best perfromance, so I began to play around with setting the value of maxOffsetsPerTrigger and found thatfaving a value somewhere between 600-1000 gave optimal performance.  I was gauging this based on the "processedRowsPerSecond, which with the configuration combination mentioned above was around 1.7
>

