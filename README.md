# Studi Kasus Apache Kafka

## Anggota Kelompok

| Nama                    | NRP        |
| ----------------------- | ---------- |
| Samuel Yuma Krismata    | 5027221029 |
| Jonathan Aditya Baswara | 5027221062 |

## Topik: Pengumpulan Data Sensor IoT dengan Apache Kafka

### Latar Belakang Masalah

Sebuah pabrik memiliki beberapa mesin yang dilengkapi sensor suhu. Data suhu dari setiap mesin perlu dipantau secara real-time untuk menghindari overheating. Setiap sensor akan mengirimkan data suhu setiap detik, dan pabrik membutuhkan sistem yang dapat mengumpulkan, menyimpan, dan menganalisis data suhu ini.

### Studi Kasus Sederhana

-   Pabrik membutuhkan aliran data sensor yang dapat diteruskan ke layanan analitik atau dashboard secara langsung.
-   Apache Kafka akan digunakan untuk menerima dan mengalirkan data suhu, sementara PySpark akan digunakan untuk mengolah dan memfilter data tersebut.

### Tugas

1. **Buat Topik Kafka untuk Data Suhu**
    - Buat topik di Apache Kafka bernama "sensor-suhu" yang akan menerima data suhu dari sensor-sensor mesin.
2. **Simulasikan Data Suhu dengan Producer**
    - Buat producer sederhana yang mensimulasikan data suhu dari beberapa sensor mesin (misalnya, 3 sensor berbeda).
    - Setiap data suhu berisi ID sensor dan suhu saat ini (misalnya, sensor_id: S1, suhu: 70°C), dan dikirim setiap detik ke topik "sensor-suhu".
3. **Konsumsi dan Olah Data dengan PySpark**
    - Buat consumer di PySpark yang membaca data dari topik "sensor-suhu".
    - Filter data suhu yang berada di atas 80°C, sebagai indikator suhu yang perlu diperhatikan.
4. **Output dan Analisis**
    - Cetak data yang suhu-nya melebihi 80°C sebagai tanda peringatan sederhana di console.

## Prasyarat

-   Docker
-   Hadoop
-   Java 21 (Open JDK 21)
-   Python library: kafka, pyspark

## Konfigurasi Proyek

Instalasi Apache Kafka beserta Zookeeper pada aplikasi Docker dapat dilakukan dengan menggunakan file `docker-compose.yml` dengan konfigurasi sebagai berikut:

```yml
version: "2"

services:
    zookeeper:
        image: wurstmeister/zookeeper:latest
        ports:
            - "2181:2181"

    kafka:
        image: wurstmeister/kafka:latest
        ports:
            - "9092:9092"
        expose:
            - "9093"
        environment:
            KAFKA_ADVERTISED_LISTENERS: INSIDE://kafka:9093,OUTSIDE://localhost:9092
            KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INSIDE:PLAINTEXT,OUTSIDE:PLAINTEXT
            KAFKA_LISTENERS: INSIDE://0.0.0.0:9093,OUTSIDE://0.0.0.0:9092
            KAFKA_INTER_BROKER_LISTENER_NAME: INSIDE
            KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
            KAFKA_CREATE_TOPICS: "sensor-suhu:1:1"
        volumes:
            - /var/run/docker.sock:/var/run/docker.sock
```

Gunakan command berikut untuk menjalankan container melalui file tersebut:

`docker compose up -d`

## Simulasi Studi Kasus

Gunakan command berikut untuk menjalankan producer:

`python3 producer.py`

Gunakan command berikut untuk menjalankan consumer:

`python3 consumer.py`

Berikut adalah hasil ketika producer dan consumer berhasil dijalankan:

![Screenshot](/img/screenshot.png)
