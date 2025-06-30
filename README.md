# CAN-Bus-Data-Logging-and-Analysis-Using-Python-and-SQLite
A Python-based project for real-time CAN bus data logging using a virtual CAN interface and SQLite, with message analysis and frequency visualization.

Step 1: Install Required Packages

sudo apt update
sudo apt install -y python3 python3-pip iproute2 can-utils sqlite3 sqlitebrowser
pip3 install python-can pandas matplotlib

Step 2: Setup Virtual CAN Interface (vcan0)

sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
