# jumper-nrf52-ble-example

## Setup
- Prerequisites:
    - Ubuntu 16.04
    - git
    - Python2.7
    
- Make sure you have the latest Bluez drivers installed:
    
    ```bash
    sudo apt install autotools-dev automake libtool glib2.0 libdbus-1-dev elfutils libelf-dev libdw-dev libudev-dev libjson0 libjson0-dev libical-dev libreadline-dev libbluetooth-dev libboost-python-dev libboost-all-dev
    sudo apt remove bluez
    wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.48.tar.xz
    tar xvf bluez-5.48.tar.xz
    cd bluez-5.48
    ./configure --enable-deprecated
    make
    sudo make install
    systemctl daemon-reload  
    ```
- Get this repo and install the required Python packages:
    
    ```bash
    git clone https://github.com/Jumperr-labs/jumper-nrf52-ble-example.git
    cd jumper-nrf52-ble-examples
    sudo pip install -r requirements.txt
    ```
- Last setup step: please make sure you signed up on https://vlab.jumper.io , you have a config.json file in your system and  Jumper tools are installed in your system.

### Usage
- Open 3 different terminals and run: `cd /PATH/TO/jumper-nrf52-ble-examples/`
- ***Terminal 1 -*** Start the virtual HCI device (BLE dongle): `sudo jumper ble`

    You should see the following lines printed:
    ```
    @ New Settings: 0x0a11
            powered bondable le secure-conn 
    ```
- ***Terminal 2 -*** Start the BLE gateway program: `sudo python examples/ble_peripheral/ble_app_hrs/ble_gateway.py`
- ***Terminal 3 -*** Start the virtual nRF52 device with the ble_app_hrs example:
    
    ```bash
    cd examples/ble_peripheral/ble_app_hrs/jumper/
    jumper run -b ../pca10040/s132/armgcc/_build/nrf_and_softdevice.bin -u  
    ```
- Check out the output on terminal 2:
    
    ```
    Scanning for devices
    Found device:  F6:39:AF:A3:A0:87
    connecting to:  F6:39:AF:A3:A0:87
    Connected
    Battery level: 100
    Heart rate level: 3
    Battery level: 97
    ...
    ...
    ...
    ```