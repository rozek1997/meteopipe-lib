import argparse
import logging
import time
import sys
from client import MeteoPipeClient

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()


def run():
    parser = argparse.ArgumentParser(description="Send and receive messages through and MQTT connection.")
    parser.add_argument('--config-file')
    args = parser.parse_args()
    client = MeteoPipeClient()
    try:
        client.setup(args.config_file)
    except Exception as error:
        logger.error(error)
    message_to_send = 10
    for i in range(message_to_send):
        client.publish_message({"message": "Hello from device {}".format(i)})
        time.sleep(5)

    client.close_connection()


if __name__ == "__main__":
    run()
