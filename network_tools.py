# Shows the IP on the i2c lcd screen connected
import socket
import os
import dbus


# This does not work
def create_network(ssid, password, interface='wlan0'):
    bus = dbus.SystemBus()
    wpas_obj = bus.get_object('fi.w1.wpa_supplicant1',
                            '/fi/w1/wpa_supplicant1')

    wpas = dbus.Interface(wpas_obj, 'fi.w1.wpa_supplicant1')
    path = wpas.CreateInterface({'Ifname': interface})
    if_obj = bus.get_object('fi.w1.wpa_supplicant1', path)
    path = if_obj.AddNetwork({
    'ssid':ssid,
    'mode':1,
    'frequency':2412,
    'proto':'WPA',
    'key_mgmt':'NONE',
    'pairwise':'NONE',
    'group':'TKIP',
    'psk':password,
    }, dbus_interface='fi.w1.wpa_supplicant1.Interface')

    network = bus.get_object('fi.w1.wpa_supplicant1', path)
    network.Set('fi.w1.wpa_supplicant1.Network', 'Enabled', True, dbus_interface=dbus.PROPERTIES_IFACE)
    print(network.GetAll('fi.w1.wpa_supplicant1.Network', dbus_interface=dbus.PROPERTIES_IFACE))


def get_network_ssid():
    return os.popen('sudo iwgetid -r').read()


def get_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP

