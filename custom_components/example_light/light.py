"""Platform for lights integration."""
import logging

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
# Import the device class from the component that you want to support
from homeassistant.components.light import (
    ATTR_BRIGHTNESS, PLATFORM_SCHEMA, Light)
from homeassistant.const import CONF_HOST, CONF_PASSWORD, CONF_USERNAME

_LOGGER = logging.getLogger(__name__)

# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST): cv.string,
    vol.Optional(CONF_USERNAME, default='admin'): cv.string,
    vol.Optional(CONF_PASSWORD): cv.string,
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Awesome Light platform."""
    import awesomelights

    # Assign configuration variables.
    # The configuration check takes care they are present.
    host = config[CONF_HOST]
    username = config[CONF_USERNAME]
    password = config.get(CONF_PASSWORD)

    # Setup connection with devices/cloud
    hub = awesomelights.Hub(host, username, password)

    # Verify that passed in configuration works
    if not hub.is_valid_login():
        _LOGGER.error("Could not connect to AwesomeLight hub")
        return

    # Add devices
    add_entities(AwesomeLight(light) for light in hub.lights())


class AwesomeLight(Light):
    """Representation of an Awesome Light."""

    def __init__(self, light):
        """Initialize an AwesomeLight."""
        self._light = light
        self._name = light.name
        self._state = None
        self._brightness = None

    @property
    def name(self):
        """Return the display name of this lights."""
        return self._name

    @property
    def brightness(self):
        """Return the brightness of the lights.

        This method is optional. Removing it indicates to Home Assistant
        that brightness is not supported for this lights.
        """
        return self._brightness

    @property
    def is_on(self):
        """Return true if lights is on."""
        return self._state

    def turn_on(self, **kwargs):
        """Instruct the lights to turn on.

        You can skip the brightness part if your lights does not support
        brightness control.
        """
        self._light.brightness = kwargs.get(ATTR_BRIGHTNESS, 255)
        self._light.turn_on()

    def turn_off(self, **kwargs):
        """Instruct the lights to turn off."""
        self._light.turn_off()

    def update(self):
        """Fetch new state data for this lights.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._light.update()
        self._state = self._light.is_on()
        self._brightness = self._light.brightness
