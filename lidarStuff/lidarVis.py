import matplotlib.animation as animation
import matplotlib.pyplot as plt
from rplidar import RPLidar
import numpy as np
import time

# Windows : "COM5"
# Linux   : "/dev/ttyUSB0"
# MacOS   : "/dev/tty.usbserial-0001"
PORT_NAME = '/dev/tty.usbserial-0001'
DMAX = 800
IMIN = 0
IMAX = 50

def update_line(num, iterator, line):
    leftDegLim = 60
    rightDegLim = 300
    f = open('LiDAR-LogFile-{}.txt'.format(str(timeStamp)), 'a')
    outLiDAR = next(iterator)
    logStuff = 'UnixEpoch-Time: ' + str(time.time()) + '\n' + str(outLiDAR) + '\n\n'
    f.write(logStuff)
    f.close()
    outLiDAR = np.array(outLiDAR, dtype=[('quality', 'i4'), ('angle', 'f4'), ('distance', 'f4')])
    targetMask = ((outLiDAR['angle'] >= 0) & (outLiDAR['angle'] <= leftDegLim)) | ((outLiDAR['angle'] >= rightDegLim) & (outLiDAR['angle'] <= 360))
    targetRegion = outLiDAR[targetMask]
    print(targetRegion)
    offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in outLiDAR])
    line.set_offsets(offsets)
    intens = np.array([meas[0] for meas in outLiDAR])
    line.set_array(intens)
    time.sleep(5)
    return line

def run():
    lidar = RPLidar(PORT_NAME)
    fig = plt.figure()
    ax = plt.subplot(111, projection='polar')
    line = ax.scatter([0, 0], [0, 0], s=5, c=[IMIN, IMAX],
                           cmap=plt.cm.Greys_r, lw=0)
    ax.set_rmax(DMAX)
    ax.grid(True)

    iterator = lidar.iter_scans()
    ani = animation.FuncAnimation(fig, update_line,
        fargs=(iterator, line), interval=50)
    plt.show()
    lidar.stop()
    lidar.disconnect()

if __name__ == '__main__':
    timeStamp = time.time()
    run()