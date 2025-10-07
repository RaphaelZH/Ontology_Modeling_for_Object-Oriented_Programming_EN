import paho.mqtt.client as mqtt

import mysql.connector

import json
import os
import time

broker_host = os.getenv("MQTT_BROKER_HOST", "test.mosquitto.org")
broker_port = int(os.getenv("MQTT_BROKER_PORT", 1883))


def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

    sql = "INSERT INTO heartbeat_records (datetime, heart_rate) VALUES (%s, %s)"
    val = (payload["datetime"], payload["heart_rate"])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("heart_rate/topic")
    client.on_message = handle_telemetry


def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")


def random_heart_rate():
    return 60 + int(40 * os.urandom(1)[0] / 255)  # Random heart rate between 60 and 100


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Métronome",
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute the CREATE DATABASE IF NOT EXISTS statement
sql_query = "CREATE DATABASE IF NOT EXISTS heartbeat_monitor"
mycursor.execute(sql_query)
mydb.database = "heartbeat_monitor"

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS heartbeat_records (datetime VARCHAR(255), heart_rate INT)"
)

heart_rate = random_heart_rate()
sql = "INSERT INTO heartbeat_records (datetime, heart_rate) VALUES (%s, %s)"
val = (time.strftime("%Y-%m-%d %H:%M:%S"), heart_rate)

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

for x in mycursor:
    print(x)
    mycursor.execute("SHOW COLUMNS FROM heartbeat_records")
    for col in mycursor:
        print("Column:", col)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_host, broker_port, 60)

client.loop_start()

while True:
    time.sleep(5)
