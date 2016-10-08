import imaplib, socket, dwmstatus.config

def imap_unread():
    socket.setdefaulttimeout(10)

    try:
        config = dwmstatus.config.config()
        obj = imaplib.IMAP4_SSL(config('imap_host'), config('imap_port'))
        obj.login(config('imap_user'), config('imap_password'))
        obj.select()
        unread_mail_count = len(obj.search(None, 'UnSeen')[1][0].split())
    except Exception as e:
        unread_mail_count = '-'
    return unread_mail_count
