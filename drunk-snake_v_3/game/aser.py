import socket
def bla(s, file):
    f = open("file", "r")
    for line in f:
        a = bytes(line, "utf-8")
        s.send(a)
    f.close()