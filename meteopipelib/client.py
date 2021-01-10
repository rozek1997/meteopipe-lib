from connection_mqtt import Connection
from config_file_parser import ConfigFileParser

import json


class MeteoPipeClient:

    def __init__(self):
        self.config_file_parser = ConfigFileParser()
        self.connection = Connection()

    def setup(self, config_file_path):
        config = self.config_file_parser.load_configuration_from_file(file_path=config_file_path)
        self.connection.init_connection(config)

    def close_connection(self):
        self.connection.disconnect()

    def publish_message(self, message: dict):
        json_message = json.dumps(message)
        self.connection.publish(json_message)

    def get_configuration(self):
        self.config_file_parser.get_configuration()
