from os import environ
from pathlib import Path

WORKING_DIRECTORY = Path().resolve() / "ml-service"

KAFKA_BOOTSTRAP_SERVERS = f'{environ.get("KAFKA_SERVER")}:{environ.get("BOOTSTRAP_SERVICE_PORT")}'
SCHEMA_REGISTRY_URL = f'http://{environ.get("KAFKA_SERVER")}:{environ.get("SCHEMA_REGISTRY_PORT")}'

CONSUMER_GROUP_ID = "spring-service-group"
TOPIC_CLASSIFICATION_REQUEST = "ticket.classification.request"
TOPIC_CLASSIFICATION_RESPONSE = "ticket.classification.response"

UUID_NAME = "uuid"
SUBJECT_NAME = "subject"
DESCRIPTION_NAME = "description"
