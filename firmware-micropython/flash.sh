echo "putting files on device"
ampy -p /dev/ttyACM0 put main.py
ampy -p /dev/ttyACM0 reset --hard

