from __future__ import print_function
from builtins import input
import struct
from time import sleep
import argparse
import gattlib
import pdb


# def discover(device_id):
#     discovery = gattlib.DiscoveryService(device_id)
#     devices = discovery.discover(10)
#
#     for address, name in devices.items():
#         print('Found device: {} {}'.format(name, address))
#         # print("name: {}, address: {}".format(name, address))


# class NrfRequester(gattlib.GATTRequester):
#     CHARACTARISTIC_TO_NOTIFY = "00002a19-0000-1000-8000-00805f9b34fb"  # nrf52 measurement charactaristic
#     # CHARACTARISTIC_TO_NOTIFY = "0000180f-0000-1000-8000-00805f9b34fb"  # nrf52 measurement charactaristic
#     NOTIFY_ON   = struct.pack("<H", 0x0001)
#     NOTIFY_OFF  = struct.pack("<H", 0x0000)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--adapter-name', type=str, help='Adapter name', default='hci0')
    parser.add_argument('-c', '--channel-type', type=str, help='Channel type', choices=('random', 'public'), default='random')
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
    sleep(1.5)
    input('Press enter to connect...')
    print('connecting to: {} {}'.format(device_name, bd_addr))
    req = gattlib.GATTRequester(bd_addr, False, args.adapter_name)
    req.connect(wait=True, channel_type=args.channel_type)
    print('Connected')

    previous_battery_level = 0
    try:
        while True:
            battery_level = ord(req.read_by_handle(0x16)[0])
            if battery_level != previous_battery_level:
                print('Battery level: {}'.format(battery_level))
                previous_battery_level = battery_level
            sleep(5)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
