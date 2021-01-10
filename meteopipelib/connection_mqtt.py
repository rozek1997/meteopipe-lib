import paho.mqtt.client as mqtt
import logging
import sys
import time
import json

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()


class Connection:

    def __init__(self):
        self.config = {}
        self.client = None

    def init_connection(self, configuration: dict):
        self.config = configuration
        self.client = mqtt.Client(client_id=self.config["clientId"])

        self.client.tls_set(
            ca_certs=self.config["ca_cert_path"],
            certfile=self.config["cert_path"],
            keyfile=self.config["private_key_path"],
        )

        self.client.on_connect = self.__on_connect
        self.client.on_message = self.__on_message
        self.client.on_publish = self.__on_publish
        self.client.connect(host=self.config["endpoints"], port=8883)

        self.client.loop_start()

    def publish(self, message: str):
        self.client.publish(topic=self.config["topic"], payload=message)

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

    def __on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logger.info("Client is connected: {} with code {}".format(self.client.is_connected(), rc))
            self.client.subscribe(self.config.get("topic"))
        else:
            logger.error("Connection error with error code {}".format(rc))

    def __on_message(self, client, userdata, msg):
        message = json.loads(msg.payload)
        logger.info(message)

    def __on_publish(self, client, userdata, mid):
        logger.info("Message send {}".format())
