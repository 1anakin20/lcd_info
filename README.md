# LCD Info
Shows information about the network in a connected I2C LCD

# Use a service
To run it at startup in the background, it can be added a systemd service. There is a template for a service file in lcd_info.service.
The file may go in /etc/systemd/system/. Make sure to put the correct path to the lcd_info/main.py
