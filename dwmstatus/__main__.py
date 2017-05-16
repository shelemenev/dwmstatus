import os, datetime, time
from dwmstatus.dwmstatus import *
import dwmstatus.config

def main():
    unread = -1
    num_retry = 0
    dwmstatus.config.init()
    config = dwmstatus.config.config()
    os.system('feh --bg-scale ~/source/wallpaper.jpg')
    os.system('xset s off -dpms')
    while True:
        today = datetime.datetime.today()
        if int(today.strftime('%M')) % 5 == 0 or unread < 0:
            unread = imap_unread(config)
            bat = battery()
        if unread < 0 and num_retry < 3:
            num_retry += 1
            continue
        num_retry = 0
        status = '[Mail: ' + str(unread if unread >= 0 else '-') + '] [' + bat + '] '
        today += datetime.timedelta(hours = config('utc_delta'))
        status += today.strftime('%A %Y-%m-%d %H:%M')
        os.system('xsetroot -name "' + status + '"')
        time.sleep(60)

if __name__ == "__main__":
    main()
