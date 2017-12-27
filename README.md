# jumper-nrf52-ble-example

## clone this repository
open a terminal in your ubuntu machine and run: 
```bash
git clone https://github.com/Jumperr-labs/jumper-nrf52-ble-example.git
```
### Setup
open a terminal in your ubuntu machine and run: 
```bash
sudo su

apt-get install git
wget https://bootstrap.pypa.io/ez_setup.py -O - | python
easy_install pip
pip install virtualenv
git clone git://git.kernel.org/pub/scm/bluetooth/bluez.git
apt-get install autotools-dev automake libtool glib2.0 libdbus-1-dev elfutils libelf-dev libdw-dev libudev-dev libjson0 libjson0-dev libical-dev libreadline-dev libbluetooth-dev libboost-python-dev libboost-all-dev
cd bluez && ./bootstrap-configure --disable-android --disable-midi
make install

exit

cd /PATH/TO/jumper-nrf52-ble-examples/
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Last setup step: please make sure you signed up on https://vlab.jumper.io , you have a config.json file in your system and  Jumper tools are installed in your system. Note to not install it under super user (sudo su).

#### Usage

- Open 3 different terminals, cd into jumper-nrf52-ble-examples directory and in the first two run:
    ```bash
    sudo su
    cd /PATH/TO/jumper-nrf52-ble-examples/
    source venv/bin/activate
    ```
- On the third terminal, cd into jumper-nrf52-ble-examples directory and run:
    ```bash
    cd /PATH/TO/jumper-nrf52-ble-examples/
    source venv/bin/activate
    ```
    
- ***Terminal 1 -*** Start the virtual HCI device (BLE dongle): `jumper ble`
    You should see the following lines printed:
    @ New Settings: 0x0a11
            powered bondable le secure-conn 

    if you don't see it, please hit ctrl+c and restart
- ***Terminal 2-*** Start the BLE gateway program: `python examples/ble_peripheral/ble_app_hrs/ble_gateway.py`
- ***Terminal 3-*** Start the virtual nRF52 device with the ble_app_hrs example (note that you are not in root):
    ```bash
    cd examples/ble_peripheral/ble_app_hrs/jumper/
    jumper run -b ../pca10040/s132/armgcc/_build/nrf_and_softdevice.bin  
    ```
- Go back to ***terminal 2*** and follow the instructions
