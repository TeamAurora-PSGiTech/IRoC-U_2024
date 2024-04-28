from rplidar import RPLidar

# Linux   : "/dev/ttyUSB0"
# MacOS   : "/dev/tty.usbserial-0001"
# Windows : "COM5"
lidar = RPLidar('/dev/tty.usbserial-0001')

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

for i, scan in enumerate(lidar.iter_scans()):
    print('%d: Got %d measurments' % (i, len(scan)))
    if i > 100:
        break

lidar.stop()
lidar.stop_motor()
lidar.disconnect()