# Ability Hand API - Python Examples

### System Requirements 

These examples require Python 3.10 or newer. They have been tested on Windows 10 and Ubuntu. Nothing should prevent them from working on Mac, however this is untested. Before running the examples, install the required modules using pip: `pip install -r requirements.txt` 

### Hand Setup

These examples are set up to communicate with the Ability Hand over a Serial to UART Dongle, such as a CP210x dongle. Connect Ground, TX (SDA), and RX (SCL) from the hand to the dongle. 

Before running, please ensure the hand is in UART communication mode - this can be configured over Bluetooth with the binary setting command `We16`

To enable byte stuffing, send `We46` and `We47`
add `--stuff` option when running the python scripts below.

## Included Examples

### `live_plot.py`

This example uses the Ability Hand Extended API to live plot data from the hand while providing the option to do basic hand movements with keyboard controls. It can plot either touch or position data using command line parameters to specify:
- `python3 live_plot.py --touch`
- `python3 live_plot.py --position`

When plotting touch data it uses the extended API in mode 0x10, for position data it uses 0x12. Instructions on how to move the hand will be printed to the console. This demo is set-up to be work with an Ability Hand with default out of the box settings. However, you can configure this with command line options - use `python3 live_plot.py -h` for a full list of options. 


## Common Bugs and Solutions (Linux)
### You plugged in the hand but it `Failed to Connect!`. 

Try directly connecting:
Comment out these lines in setupSerial():
```
try: 
    print("Connecting...")
    ser = serial.Serial(port[0], baud, timeout = 0)
    print("Connected!")
except: 
    print("Failed to Connect!")
    return False
```
and put this following directly:
```
ser = serial.Serial(port[0], baud, timeout = 0)
```

Most likely you have not granted permission for the hand port (mine was `/dev/ttyUSB0`).

A temporary solution (in terminal):
```
$ sudo chmod a+rw /dev/ttyUSB0
```

A perminent solution: allow non-root access to hand port:
```
sudo usermod -aG dialout $USER
```
Then RESTART your computer.

For any other connection issue, please look up online.

### `Keyboard` package permission issue
```
packages/keyboard/_nixcommon.py", line 174, in ensure_root
    raise ImportError('You must be root to use this library on linux.')
ImportError: You must be root to use this library on linux.
```
To solve this, you will need to run the USER python under SUDO.

If you don't know where your python is, in terminal:
```
$ which python3
```
You might get: `/usr/bin/python3`. Then run like this:
```
$ sudo /usr/bin/python3 live_plot.py --position --suff
```