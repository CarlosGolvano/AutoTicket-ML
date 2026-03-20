import logging
import os

from logging import getLogger, DEBUG, INFO
from confluent_kafka import Producer


logging.basicConfig(level=INFO)
logger = getLogger(__name__)

config = {
    'bootstrap.servers': f'{os.environ.get("KAFKA_SERVER")}:29093',
    'logger': logger,
    'debug': "broker,topic,metadata"
}

producer = Producer(config)


def delivery_report(err, msg):
    if err:
        print(f"Error enviando mensaje: {err}")
    else:
        print(f"Mensaje enviado a {msg.topic()} [{msg.partition()}] offset {msg.offset()}")


producer.produce(
    topic='pruebas',
    key='alguna-clave',
    value='Mensaje de prueba',
    callback=delivery_report,
)

producer.poll(0)

producer.flush()
