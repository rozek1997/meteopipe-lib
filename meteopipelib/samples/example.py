import argparse
import logging
import time
import sys
from client import MeteoPipeClient


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()


def run():
    parser = argparse.ArgumentParser(description="Send and receive messages through and MQTT connection.")
    parser.add_argument('--config-file',
                        default="/mnt/8C0C14210C1408BA/Projects/MeteoPipeLib/26658f2f-b1e5-4043-b22a-95d76ac2d3ef/config.json")
    args = parser.parse_args()
    client = MeteoPipeClient()
    try:
        client.setup(args.config_file)
    except Exception as error:
        logger.error(error)
    else:
        message_to_send = 10
        for i in range(message_to_send):

            client.publish_message({"temparature": 40, "pressure": 1013, "visibilty": 50 })
            time.sleep(5)

        client.close_connection()


if __name__ == "__main__":
    run()
