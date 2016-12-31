# Spark RealTime Tracking :

Listed below are the dependencies, and the packages needed to run this application :

1- The kafka-python package : Official repo here https://github.com/dpkp/kafka-python or simply add it from python console as follows 
"pip install kafka-python"

2- The Mongo Spark connector : Official repo here https://github.com/mongodb/mongo-spark compatible with MongoDB 2.6 or later and Apache Spark version 1.6.x or later , check https://docs.mongodb.com/spark-connector/v1.1/ for the docs and the installation.

  a- The actual connector jar at http://search.maven.org/#search%7Cga%7C1%7Cg%3Aorg.mongodb.spark
  Make sure you get the right package, according to your scala and spark versions
  
  b- The driver and it's dependencies (manually without SBT or maven) :

    - The driver : https://oss.sonatype.org/content/repositories/releases/org/mongodb/mongodb-driver/

    - The driver core : https://oss.sonatype.org/content/repositories/releases/org/mongodb/mongodb-driver-core

    - The bson jar : https://oss.sonatype.org/content/repositories/releases/org/mongodb/bson/
  
  
Launching the app : 
  Create a kafka topic named "test" (Or use your own topic and change the code) , launch the pyspark with the following command : 

    pyspark --conf spark.mongodb.input.uri=mongodb://127.0.0.1/db_name.collection_name --conf spark.mongodb.output.uri=mongodb://127.0.0.1/db_name.collection_name --packages org.mongodb.spark:mongo-spark-connector_2.x:X.X.X
  
  Make sure you have the right db_name and collection name. Add the port number if it's different from the default one 27017.
Start the producer, and start the spark app .

I added 2 fields in the mongo objects created by the app : produced_at and processed_at for testing (speed mostly), and also 2 outputs
from the spark app that will show on the console where it was launched,to also test the writing to mongo speed.

If you want to have and make your own coordinates you can check this website http://gebweb.net/optimap/ :
  - First Mark on the map the itinerary you want to follow
  - Second Calculate the Fastest A-Z Trip
  - Export-> Toggle Raw path output
  - Copy the coordinates to the file "streaming_coordinates.txt"
  
