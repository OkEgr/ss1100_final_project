command_dict = {
    "Reaction Control Subsystem": {
        "Code": "RCS",
        "Commands": {"CMD01":['THRUST_X', range(0,60)],
                     "CMD02":['THRUST_Y', range(0,60)],
                     "CMD03":['THRUST_Z', range(0,60)],
                     "CMD04":['SAFE_MODE', {0, 1}]}
    },
    "Thermal Control Subsystem": {
        "Code": "TCS",
        "Commands": {"CMD01":['HEATER_ON', {0, 1}],
                     "CMD02":['HEATER_OFF', {0, 1}],
                     "CMD03":['VENT_OPEN_RADIATOR', {0, 1}],
                     "CMD04":['TEMP_SETPOINT', range(-30,60)]}
    },
    "Attitude Control Subsystem": {
        "Code": "ACS",
        "Commands": {"CMD01":['ROTATE_X', range(-360,360)],
                     "CMD02":['ROTATE_Y', range(-360,360)],
                     "CMD03":['ROTATE_Z', range(-360,360)],
                     "CMD04":['SAFE_MODE', {0, 1}]}
    },
    "Command & Data Handling": {
        "Code": "CDH",
        "Commands": {"CMD01":['TRANSMIT_HIGH', {0, 1}],
                     "CMD02":['TRANSMIT_LOW', {0, 1}],
                     "CMD03":['RECEIVE_MODE',{0, 1}],
                     "CMD04":['SAFE_MODE', {0,1}]}
    },
    "Telemetry, Tracking, & Command": {
        "Code": "TTC",
        "Commands": {"CMD01":['TRANSMIT_MODE', {0,1}],
                     "CMD02":['RECEIVE_MODE', {0,1}],
                     "CMD03":['TRACKING_MODE', {0,1}],
                     "CMD04":['SAFE_MODE', {0,1}]}
    },
    "Electrical Power Subsystem": {
        "Code": "EPS",
        "Commands": {"CMD01":['BATTERY_CHARGE_MODE', {0,1}],
                     "CMD02":['POWER_ON_MODULE', {0,1,2,3,4}],
                     "CMD03":['POWER_OFF_MODULE', {0,1,2,3,4}],
                     "CMD04":['VOLTAGE_SETPOINT', range(0,120)]}
    },
    "Payload System 1": {
        "Code": "PL1",
        "Commands": {"CMD01":['START_DATA_ACQUISITION', {0,1}],
                     "CMD02":['STOP_DATA_ACQUISITION', {0,1}],
                     "CMD03":['CALIBRATE_SENSOR', {0,1}],
                     "CMD04":['SAFE_MODE', {0,1}]}
    },
    "Payload System 2": {
        "Code": "PL2",
        "Commands": {"CMD01":['START_DATA_ACQUISITION', {0,1}],
                     "CMD02":['STOP_DATA_ACQUISITION', {0,1}],
                     "CMD03":['CALIBRATE_SENSOR', {0,1}],
                     "CMD04":['SAFE_MODE', {0,1}]}
    }
}