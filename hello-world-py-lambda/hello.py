"""Sample lambda function."""
import json
import logging

LOGGING_DEFAULT_LEVEL = logging.DEBUG
LOGGING_FORMAT = r"%(asctime)s-%(relativeCreated)04d [%(levelname)s] %(name)s " \
                 r"%(thread)d-%(threadName)s-%(process)d-8s %(pathname)s/%(lineno)s %(message)s"

logging.basicConfig(level=LOGGING_DEFAULT_LEVEL, format=LOGGING_FORMAT)
logger = logging.getLogger("my-test-handler")


def my_test_handler(context, event):
    logger.info(f"Event: {context}")
    logger.info(f"Event: {event}")

    response_message = "Hello, World"

    return {
        "statusCode": 200,
        "headers": {
            'Content-Type': 'application/json',
        },
        "body": json.dumps({
            "message": response_message,
        })
    }
