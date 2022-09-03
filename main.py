#!/usr/bin/env python3
from lcd_tools import LCD
import network_tools
import time
import os
import signal

# Settings
network_interface = 'wlan0'
max_connection_fails = 0
connection_timeout_seconds = 30
# Adhoc network settings
adhoc_ssid = ''
adhoc_password = ''

running = True

lcd = LCD()


def shutdown(signal, frame):
    lcd.new_screen()
    exit(0)


def is_connected():
    ip = network_tools.get_ip()
    return ip != '127.0.0.1'


def main():
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)
    lcd.new_screen()
    while (True):
        ip = network_tools.get_ip()
        if is_connected():
            # Managed to connect, Show information about the network
            network_ssid = network_tools.get_network_ssid()
            lcd.new_screen(
                [f'SSID:{network_ssid}',
                f'IP:{ip}'])
           

if __name__ == '__main__':
    main()
