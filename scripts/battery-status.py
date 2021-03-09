# coding=utf-8
import psutil

battery = psutil.sensors_battery()

percentage = round(battery.percent)

charging = battery.power_plugged
icon = ""

if charging == False:
    if percentage < 20:
        icon = ""
    elif 20 < percentage < 40:
        icon = ""
    elif 40 < percentage < 70:
        icon = ""
    elif 70 < percentage < 99:
        icon = ""
    elif percentage == 100:
        icon = ""
else:
    if percentage < 99:
        icon = ""
    else:
        icon = ""

print("{0} {1}%".format(icon, percentage))
