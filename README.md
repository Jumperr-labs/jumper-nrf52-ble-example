# jumper-nrf52-ble-example

## Setup

```bash
sudo su
cd /PATH/TO/jumper-nrf52-ble-examples/
virtualenv venv
source venv/bin/activate
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
    cd cd examples/ble_peripheral/ble_app_hrs/jumper/
    jumper run -b
    jumper run -b ../pca10040/s132/armgcc/_build/nrf_and_softdevice.bin  
    ```
- Go back to ***terminal 2*** and follow the instructions