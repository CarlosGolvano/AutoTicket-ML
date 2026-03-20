import time
from confluent_kafka.avro import AvroProducer, load as load_avro
from config import KAFKA_BOOTSTRAP_SERVERS, SCHEMA_REGISTRY_URL, TOPIC_CLASSIFICATION_RESPONSE, WORKING_DIRECTORY

PROCESSING_SCHEMA = load_avro(WORKING_DIRECTORY / "schemas/TicketProcessingEvent.avsc")
COMPLETED_SCHEMA = load_avro(WORKING_DIRECTORY / "schemas/TicketCompletedEvent.avsc")
FAILED_SCHEMA = load_avro(WORKING_DIRECTORY / "schemas/TicketFailedEvent.avsc")


def create_producer():
    return AvroProducer({
        "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
        "schema.registry.url": SCHEMA_REGISTRY_URL,
    })


def _send(producer, value, schema):
    producer.produce(
        topic=TOPIC_CLASSIFICATION_RESPONSE,
        value=value,
        value_schema=schema,
    )
    producer.flush()


def send_processing(producer, uuid):
    _send(producer, {
        "uuid": uuid,
        "timestamp": int(time.time() * 1000),
    }, PROCESSING_SCHEMA)


def send_completed(producer, uuid, category, sentiment, urgency):
    _send(producer, {
        "uuid": uuid,
        "category": category,
        "sentiment": sentiment,
        "urgency": urgency,
        "timestamp": int(time.time() * 1000),
    }, COMPLETED_SCHEMA)


def send_failed(producer, uuid):
    _send(producer, {
        "uuid": uuid,
        "timestamp": int(time.time() * 1000),
    }, FAILED_SCHEMA)
