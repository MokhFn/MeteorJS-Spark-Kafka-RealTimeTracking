from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SQLContext
import datetime
ssc = StreamingContext(sc, 1)
kvs = KafkaUtils.createDirectStream(ssc, ["test"], {"bootstrap.servers": "localhost:9092"})
lines = kvs.map(lambda x: x[1])
coords = lines.map(lambda line: line.split(" "))
data = coords.map(lambda coord: (float(coord[1]),float(coord[3]),str(" ".join(coord[5:7])),str(datetime.datetime.now()).split('.')[0]))
data.pprint()
def saveCoord(rdd):
    if (rdd.count() != 0) :
        coord = sqlContext.createDataFrame(rdd, ["long", "lat", "produced_at" , "processed_at"])
        print str(datetime.datetime.now()).split('.')[0]
        coord.write.format("com.mongodb.spark.sql").mode("append").save()
        print str(datetime.datetime.now()).split('.')[0]
data.foreachRDD(saveCoord)
ssc.start()
ssc.awaitTermination()
