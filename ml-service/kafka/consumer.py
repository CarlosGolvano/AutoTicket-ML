from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer
from confluent_kafka.serialization import StringDeserializer
from config import KAFKA_BOOTSTRAP_SERVERS, SCHEMA_REGISTRY_URL, CONSUMER_GROUP_ID, TOPIC_CLASSIFICATION_REQUEST


def create_consumer():
    schema_registry = SchemaRegistryClient({"url": SCHEMA_REGISTRY_URL})

    consumer = DeserializingConsumer({
        "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
        "group.id": CONSUMER_GROUP_ID,
        "auto.offset.reset": "earliest",
        "key.deserializer": StringDeserializer("utf_8"),
        "value.deserializer": AvroDeserializer(schema_registry),
    })
    consumer.subscribe([TOPIC_CLASSIFICATION_REQUEST])
    return consumer


def poll_message(consumer, timeout=1.0):
    msg = consumer.poll(timeout)

    if msg is None:
        return None

    if msg.error():
        raise Exception(f"Kafka error: {msg.error()}")

    return msg.value()
