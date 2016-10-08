import os, json

def config():
    f = open(os.path.expanduser('~') + '/.config/dwmstatus')
    c = json.loads(f.read())
    f.close()
    return lambda x: c[x]
