# SF-Crime-Statistics-with-Spark-Streaming

Run in Udacity workspace environment.

Step 1:
Open new console and run: ./start.sh

Step 2:
Open new console and run: /usr/bin/zookeeper-server-start config/zookeeper.properties

Step 3:
Open new console and run: python kafka_server.py 

Step 4:
Open new console and run: /usr/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sf.police.callsforsvc --from-beginning

Step 5:
Open new console and run: spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py

Screen Shots:



Questions:

How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
