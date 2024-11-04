from kafka import KafkaProducer
import json
import time
import random

# Inisialisasi producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Daftar sensor
sensor_ids = ['PC', 'SERVER', 'ROUTER']

try:
    while True:
        for sensor_id in sensor_ids:
            # Simulasi suhu antara 60°C hingga 100°C
            suhu = round(random.uniform(60, 100), 2)
            data = {'sensor_id': sensor_id, 'suhu': suhu}
            # Mengirim data ke topik "sensor-suhu"
            producer.send('sensor-suhu', value=data)
            print(f"Data dikirim: {data}")
        # Interval pengiriman setiap 1 detik
        time.sleep(1)
except KeyboardInterrupt:
    producer.close()
