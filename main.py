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

def try_connection():
    # last_connection_attempt = time.time()
    connection_fails = 0
    while (not is_connected()):
        # Try to restart the network adapter
        # Creating ad-hoc network does not work
        if True: # connection_fails < max_connection_fails:
            connection_fails += 1
            print(f'Try {connection_fails}/{max_connection_fails}')
            lcd.new_screen([f'Try {connection_fails}/{max_connection_fails}'])
            os.system(f'sudo ifconfig {network_interface} down')
            time.sleep(1)
            os.system(f'sudo ifconfig {network_interface} up')
            time.sleep(connection_timeout_seconds)
        elif connection_fails >= max_connection_fails:
            # TODO start own network
            lcd.new_screen(['No connection', 'starting network'])
            network_tools.create_network(adhoc_ssid, adhoc_password)
            lcd.new_screen([f'adhoc ssid:{adhoc_ssid}', 'passkey:{adhoc_password}'])

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
        else:
            # Not having an IP address, try to connect to a network
            try_connection()
            

if __name__ == '__main__':
    main()
