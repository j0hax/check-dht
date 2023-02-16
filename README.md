# dht22-nagios
Nagios Plugin for monitoring temperature and humidity from a Raspberry Pi

**Notice:** This plugin works in conjuction with the [dht22](https://github.com/j0hax/dht22) project!

## Install
This software has two dependencies:

1. [pySerial](https://pyserial.readthedocs.io/en/stable/)
2. [nagiosplugin](https://nagiosplugin.readthedocs.io/en/stable/)

Both should be available for installation from your distribution's package manager and `pip`.

### openSUSE Quick Start
Following commands install dependencies, copy the script to Nagios' plugins and set it as executable:

```console
$ sudo zypper in python3-pyserial python3-nagiosplugin
$ cp check_dht.py /usr/lib/nagios/plugins/check_dht
$ chmod +x /usr/lib/nagios/plugins/check_dht
```

## Overview
### Example output with default parameters
```console
$ ./check_dht
DHT OK - 24.2 °C | error=0 humidity=34.9;40;50;0;100 temperature=24.2;30;40;-40;80
```

### Usage
```console
$ ./check_dht -h
usage: check_dht [-h] [-p PORT] [-b BAUD] [-w TEMP] [-c TEMP]
                 [--humidity-warning PERCENT] [--humidity-critical PERCENT]

Nagios Plugin to monitor DHT22/AM2302 data

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  the serial file to read from
  -b BAUD, --baud BAUD  baudrate of the serial port
  -w TEMP, --warning TEMP
                        return warning if air temperature is outside TEMP
  -c TEMP, --critical TEMP
                        return critical if air temperature is outside TEMP
  --humidity-warning PERCENT
                        return warning if humidity is outside PERCENT
  --humidity-critical PERCENT
                        return critical if humidity is outside PERCENT

(c) Johannes Arnold 2023. This software is published under the terms of the
GNU GPLv3. For the companion project to this plugin, see
https://github.com/j0hax/dht22
```


