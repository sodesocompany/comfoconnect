# API contants

FAN_MODE_AWAY = 'away'
FAN_MODE_LOW = 'low'
FAN_MODE_MEDIUM = 'medium'
FAN_MODE_HIGH = 'high'

# Commands

CMD_FAN_MODE_AWAY =    b'\x84\x15\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00'
CMD_FAN_MODE_LOW =     b'\x84\x15\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x01'
CMD_FAN_MODE_MEDIUM =  b'\x84\x15\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x02'
CMD_FAN_MODE_HIGH =    b'\x84\x15\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x03'
CMD_MODE_AUTO =        b'\x85\x15\x08\x01'
CMD_MODE_MANUAL =      b'\x84\x15\x08\x01\x00\x00\x00\x00\x01\x00\x00\x00\x01'
CMD_VENTMODE_SUPPLY =  b'\x84\x15\x06\x01\x00\x00\x00\x00\x10\x0e\x00\x00\x01'
CMD_VENTMODE_BALANCE = b'\x85\x15\x06\x01'
CMD_TEMPPROF_NORMAL =  b'\x84\x15\x03\x01\x00\x00\x00\x00\xff\xff\xff\xff\x00'
CMD_TEMPPROF_COOL =    b'\x84\x15\x03\x01\x00\x00\x00\x00\xff\xff\xff\xff\x01'
CMD_TEMPPROF_WARM =    b'\x84\x15\x03\x01\x00\x00\x00\x00\xff\xff\xff\xff\x02'
CMD_BYPASS_ON =        b'\x84\x15\x02\x01\x00\x00\x00\x00\x10\x0e\x00\x00\x01'
CMD_BYPASS_OFF =       b'\x84\x15\x02\x01\x00\x00\x00\x00\x10\x0e\x00\x00\x02'
CMD_BYPASS_AUTO =      b'\x85\x15\x02\x01'
CMD_SENSOR_TEMP_OFF =  b'\x03\x1d\x01\x04\x00'
CMD_SENSOR_TEMP_AUTO = b'\x03\x1d\x01\x04\x01'
CMD_SENSOR_TEMP_ON =   b'\x03\x1d\x01\x04\x02'
CMD_SENSOR_HUMC_OFF =  b'\x03\x1d\x01\x06\x00'
CMD_SENSOR_HUMC_AUTO = b'\x03\x1d\x01\x06\x01'
CMD_SENSOR_HUMC_ON =   b'\x03\x1d\x01\x06\x02'
CMD_SENSOR_HUMP_OFF =  b'\x03\x1d\x01\x07\x00'
CMD_SENSOR_HUMP_AUTO = b'\x03\x1d\x01\x07\x01'
CMD_SENSOR_HUMP_ON =   b'\x03\x1d\x01\x07\x02'

# Sensor locations

SENSOR_TEMPERATURE_SUPPLY = 221
SENSOR_TEMPERATURE_EXTRACT = 274
SENSOR_TEMPERATURE_EXHAUST = 275
SENSOR_TEMPERATURE_OUTDOOR = 276
SENSOR_HUMIDITY_EXTRACT = 290
SENSOR_HUMIDITY_EXHAUST = 291
SENSOR_HUMIDITY_OUTDOOR = 292
SENSOR_HUMIDITY_SUPPLY = 294
SENSOR_FAN_NEXT_CHANGE = 81
SENSOR_FAN_SPEED_MODE = 65
SENSOR_FAN_EXHAUST_DUTY = 117
SENSOR_FAN_SUPPLY_DUTY = 118
SENSOR_FAN_EXHAUST_FLOW = 119
SENSOR_FAN_SUPPLY_FLOW = 120
SENSOR_FAN_EXHAUST_SPEED = 121
SENSOR_FAN_SUPPLY_SPEED = 122
SENSOR_POWER_CURRENT = 128
SENSOR_POWER_TOTAL_YEAR = 129
SENSOR_POWER_TOTAL = 130
SENSOR_AVOIDED_HEATING_CURRENT = 213
SENSOR_AVOIDED_HEATING_TOTAL_YEAR = 214
SENSOR_AVOIDED_HEATING_TOTAL = 215
SENSOR_DAYS_TO_REPLACE_FILTER = 192
SENSOR_BYPASS_STATE = 227