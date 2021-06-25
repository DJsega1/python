from matplotlib import pyplot as plt
from matplotlib import dates
import argparse
import serial
import datetime as dt
import ctypes
from math import sqrt, acos, cos, sin

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

parser = argparse.ArgumentParser()
parser.add_argument('serial_port', type=str)
parser.add_argument('baudRate', type=int)
parser.add_argument('impacts_file', type=str)
args = parser.parse_args()
SERIAL_PORT_NAME, SERIAL_PORT_SPEED, impacts_file = args.serial_port, args.baudRate, args.impacts_file
ser = serial.Serial(SERIAL_PORT_NAME, SERIAL_PORT_SPEED, timeout=0.5)

plt.rcParams['animation.html'] = 'jshtml'
fmt = dates.DateFormatter('%H:%M:%S')
fig = plt.figure()
suplt_rssi = fig.add_subplot(212)
suplt_term = fig.add_subplot(221)
suplt_alt = fig.add_subplot(222)
fig.show()
suplt_rssi.xaxis.set_major_formatter(fmt)
suplt_rssi.set_ylabel('RSSI')
suplt_rssi.set_xlabel('Time')
suplt_rssi.set_ylim([0, 127])
suplt_alt.set_ylim([0, 34000])
suplt_alt.set_ylabel('Altitude')
suplt_term.set_ylim([0, 80])
suplt_term.set_ylabel('°C')
fig.autofmt_xdate()
dates, rssis, temps, alts, lons, lats = [], [], [], [], [], []
places = open(impacts_file, 'w')


def impact_place():
    delta_s = sqrt((lons[-1] - lons[-2]) ** 2 + (lats[-1] - lats[-2]) ** 2)
    delta_h = alts[-2] - alts[-1]
    s_full = (delta_s * alts[-1]) / delta_h
    azimut = acos((lons[-1] * lons[-2] + lats[-1] * lats[-2]) /
                  (sqrt(lons[-1] ** 2 + lats[-2] ** 2) * sqrt(lats[-1] ** 2 + lons[-2] ** 2)))
    lon_impact = lons[-2] + s_full * cos(azimut)
    lat_impact = lats[-2] + s_full * sin(azimut)
    print(f'\033[1;32mNew approximate landing place: {lon_impact} {lat_impact}\033[0;0m\n'
          f'\033[1;32mLogged to {impacts_file}\033[0;0m')
    places.write(str(lon_impact) + ' ' + str(lat_impact) + '\n')


while ser.isOpen():
    data = ser.readline().decode("utf-8")[:-4]
    if data != '' and ';' in data:
        elements = data.split(';')
        print("\033[96m" + data + "\033[0m")
        if elements[0] != '00.00.00':
            dates.append(dt.datetime.strptime(elements[1], "%H:%M:%S"))
            rssis.append(int(elements[-3]))
            temps.append(float(elements[10]))
            alts.append(float(elements[-4]))
            suplt_rssi.plot(dates, rssis, color='g')
            suplt_term.plot(dates, temps, color='b')
            suplt_alt.plot(dates, alts, color='r')
            suplt_alt.yaxis.set_tick_params(labelleft=False, labelright=True)
            fig.canvas.draw()
            plt.pause(0.1)
        if len(alts) > 1 and alts[-2] - alts[-1] >= 20:
            print("\033[1;31mFALLING!\033[0;0m")
            impact_place()
