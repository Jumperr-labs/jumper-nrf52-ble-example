from __future__ import print_function
from time import sleep
import argparse
import gattlib
import pygatt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--adapter-name', type=str, help='Adapter name', default='hci0')
    args = parser.parse_args()

    print('Scanning for devices')
    service = gattlib.DiscoveryService(args.adapter_name)
    bd_addr = ''
    device_name = ''

    while bd_addr == '':
        devices = service.discover(4)
        for address, name in devices.items():
            bd_addr = address
            device_name = name

    print('Found device: {} {}'.format(device_name, bd_addr))
    print('connecting to: {} {}'.format(device_name, bd_addr))
    
    previous_battery_level = 0
    previous_hr_level = 0
    adapter = pygatt.GATTToolBackend()

    try:
        adapter.start()
        
        device = adapter.connect(bd_addr, timeout=20, address_type=pygatt.BLEAddressType.random)
        # use this to connect to a specific device:
        # device = adapter.connect('FC:A0:D7:76:E0:53', timeout=20, address_type=pygatt.BLEAddressType.random)
        print('Connected')

        while True:
            battery_level = ord(device.char_read("00002a19-0000-1000-8000-00805f9b34fb", timeout=20))
            if battery_level != previous_battery_level:
                print('Battery level: {}'.format(battery_level))
                previous_battery_level = battery_level
            hr_level = ord(device.char_read("00002a38-0000-1000-8000-00805f9b34fb", timeout=20))
            if hr_level != previous_hr_level:
                print('Heart rate level: {}'.format(hr_level))
                previous_hr_level = hr_level
            sleep(5)
    except KeyboardInterrupt:
        pass
    finally:
        print('Disconnecting')
        adapter.stop()


if __name__ == '__main__':
    main()
