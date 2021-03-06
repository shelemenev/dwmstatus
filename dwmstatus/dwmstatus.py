import imaplib, socket, dwmstatus.config, subprocess, re

def imap_unread(config):
    socket.setdefaulttimeout(10)

    try:
        obj = imaplib.IMAP4_SSL(config('imap_host'), config('imap_port'))
        obj.login(config('imap_user'), config('imap_password'))
        obj.select()
        unread_mail_count = len(obj.search(None, 'UnSeen')[1][0].split())
    except Exception as e:
        unread_mail_count = -1
    return unread_mail_count

def battery():
    return re.sub('[^0-9%]', '', subprocess.getoutput('upower -i $(upower -e | grep BAT) | grep percentage'))
