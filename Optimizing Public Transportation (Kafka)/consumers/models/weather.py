"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""

        #
        #
        # TODO: Process incoming weather messages. Set the temperature and status.
        #
        #
        if "weather" in message.topic():
            weather = json.loads(message.value())
            try:
                self.temperature = weather["temperature"]
                self.status = weather.get["status"]
            except KeyError as e:
                logger.info("weather process_message is incomplete - skipping")
                logger.debug(f"Failed to unpack message {e}")