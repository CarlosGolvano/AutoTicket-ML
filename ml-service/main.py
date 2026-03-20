import logging

from confluent_kafka.avro import load as load_avro
from kafka.consumer import create_consumer, poll_message
from kafka.producer import create_producer, send_processing, send_completed, send_failed
from config import UUID_NAME, SUBJECT_NAME, DESCRIPTION_NAME, WORKING_DIRECTORY

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

RESPONSE_SCHEMA = load_avro(WORKING_DIRECTORY / "schemas/TicketCompletedEvent.avsc")


def handle_message(producer, message):
    uuid = message[UUID_NAME]
    subject = message[SUBJECT_NAME]
    description = message[DESCRIPTION_NAME]

    send_processing(producer, uuid)
    logger.info(f"Ticket received: {uuid} [{subject}] [{description}]")

    try:
        # Temp return
        category = "CONSULTA_GENERAL"
        sentiment = "NEUTRAL"
        urgency = "LOW"

        send_completed(producer, uuid, category, sentiment, urgency)
        logger.info(f"Ticket {uuid} → category={category}, sentiment={sentiment}, urgency={urgency}")
    except Exception as e:
        send_failed(producer, uuid)
        logger.error(f"Ticket with {uuid} failed {e}", exc_info=True)


def main():
    consumer = create_consumer()
    producer = create_producer()

    logger.info("ML service init. Waiting for messages...")

    try:
        while True:
            message = poll_message(consumer)

            if message is None:
                continue

            try:
                handle_message(producer, message)
            except Exception as e:
                logger.error(f"Error processing message: {e}", exc_info=True)

    except KeyboardInterrupt:
        logger.info("Shuting down ML service...")
    finally:
        consumer.close()


if __name__ == "__main__":
    main()
