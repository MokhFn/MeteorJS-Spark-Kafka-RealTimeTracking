from kafka import KafkaProducer
from time import sleep

filename = "C:\Users\Mokh\Desktop\streaming_coordinates.txt"
coordinates = open(filename).read().splitlines()

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for line in coordinates:
    parsed_line = line.split("(")[1].split(")")[0].split(", ")
    print parsed_line
    producer.send('test', b'LG '+parsed_line[1]+' LT '+parsed_line[0])
    #sleep(5)

producer.flush()


