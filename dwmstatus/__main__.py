import os, datetime, time
from dwmstatus.dwmstatus import *

def main():
    unread = -1
    num_retry = 0
    while True:
        today = datetime.datetime.today()
        if int(today.strftime('%M')) % 5 == 0 or unread < 0:
            unread = imap_unread()
        if unread < 0 and num_retry < 3:
            num_retry += 1
            continue
        num_retry = 0
        status = '[Mail: ' + str(unread if unread >= 0 else '-') + '] '
        status += today.strftime('%Y-%m-%d %H:%M')
        os.system('xsetroot -name "' + status + '"')
        time.sleep(60)

if __name__ == "__main__":
    main()
