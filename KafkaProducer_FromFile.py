from kafka import KafkaProducer
from time import sleep
import datetime

filename = "streaming_coordinates.txt"
coordinates = open(filename).read().splitlines()

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for line in coordinates:
    parsed_line = line.split("(")[1].split(")")[0].split(", ")
    # Uncomment the two following lines for more output, and to keep track of what's actually happening
    #print parsed_line
    #print 'LG '+parsed_line[1]+' LT '+parsed_line[0]+' PT '+str(datetime.datetime.now()).split('.')[0]
    producer.send('test', 'LG '+parsed_line[1]+' LT '+parsed_line[0]+' PT '+str(datetime.datetime.now()).split('.')[0])
    sleep(5)

producer.flush()
