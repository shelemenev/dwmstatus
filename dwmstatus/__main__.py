import os, datetime, time
from dwmstatus.dwmstatus import *

def main():
    unread = imap_unread()
    while True:
        status = '[Mail: ' + str(unread) + '] '
        today = datetime.datetime.today()
        status += today.strftime('%Y-%m-%d %H:%M')
        os.system('xsetroot -name "' + status + '"')
        if int(today.strftime('%M')) % 5 == 0:
            unread = imap_unread()
        time.sleep(60)

if __name__ == "__main__":
    main()
