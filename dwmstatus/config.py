import os, json

c = {}

def init():
    global c
    f = open(os.path.expanduser('~') + '/.config/dwmstatus')
    c = json.loads(f.read())
    f.close()

def config():
    return lambda x: c[x]
