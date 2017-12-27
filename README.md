# jumper-nrf52-ble-example

## Setup

```bash
sudo su

apt-get install git
wget https://bootstrap.pypa.io/ez_setup.py -O - | python
easy_install pip
pip install virtualenv
git clone git://git.kernel.org/pub/scm/bluetooth/bluez.git
apt-get install autotools-dev automake libtool glib2.0 libdbus-1-dev elfutils libelf-dev libdw-dev libudev-dev libjson0 libjson0-dev libical-dev libreadline-dev
./bootstrap-configure --disable-android --disable-midi
make install

cd /PATH/TO/jumper-nrf52-ble-examples/
virtualenv venv
source venv/bin/activate
apt-get install libbluetooth-dev libboost-python-dev libboost-all-dev
pip install -r requirements.txt
```

### Usage

- Open 3 different terminals, cd into jumper-nrf52-ble-examples directory and in all of them run:
    ```bash
    sudo su
    cd /PATH/TO/jumper-nrf52-ble-examples/
    source venv/bin/activate
    ```
- ***Terminal 1 -*** Start the virtual HCI device (BLE dongle): `jumper hci`
- ***Terminal 2-*** Start the BLE gateway program: `python examples/ble_peripheral/ble_app_hrs/ble_gateway.py`
- ***Terminal 3-*** Start the virtual nRF52 device with the ble_app_hrs example:
    ```bash
    cd examples/ble_peripheral/ble_app_hrs/jumper/
    jumper run -b ../pca10040/s132/armgcc/_build/nrf_and_softdevice.bin  
    ```
- Go back to ***terminal 2*** and follow the instructions
