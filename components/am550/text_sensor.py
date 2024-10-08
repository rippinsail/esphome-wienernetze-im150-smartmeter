import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor
from esphome.const import *
from . import AM550_COMPONENT_SCHEMA, CONF_AM550_ID

T_SENSORS = [
    "active_energy_pos",
    "active_energy_neg",
    "reactive_energy_pos",
    "reactive_energy_neg"
]

CONFIG_SCHEMA = AM550_COMPONENT_SCHEMA.extend(
    {cv.Optional(t): text_sensor.text_sensor_schema() for t in T_SENSORS}
)


async def to_code(config):
    paren = await cg.get_variable(config[CONF_AM550_ID])

    for t in T_SENSORS:
        if t in config:
            conf = config[t]
            sens = await text_sensor.new_text_sensor(conf)
            cg.add(getattr(paren, f"set_{t}_raw")(sens))
