import logging
import json
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ConfigFileParser:

    def __init__(self):
        self.configuration = {}

    def load_configuration_from_file(self, file_path):
        config_unparsed = self.__load_config_file(file_path)
        self.__parse_configuration(config_unparsed)
        self.__check_configuration()
        return self.configuration

    def get_configuration(self):
        return self.configuration

    def __load_config_file(self, file_path):
        try:
            with open(file_path, "r") as config_file:
                config = config_file.read()
        except EnvironmentError as error:
            logger.error(error)
        else:
            config_file.close()

        return config

    def __parse_configuration(self, config_string: str):
        config_temp = json.loads(config_string)
        self.configuration = config_temp

    def __check_configuration(self):
        config = self.configuration
        value = False
        value = config["clientId"]
        value = config["endpoints"]
        value = config["topic"]
        value = config["public_key_path"]
        value = config["private_key_path"]
        value = config["cert_path"]
        value = config["ca_cert_path"]
        # value = config["location"]
