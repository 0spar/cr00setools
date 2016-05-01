import socket
import telnetlib
from hexdump import hexdump

s = socket.create_connection(("127.0.0.1", 4000))

def q(x):
  return struct.pack("I", x)

def Q(x):
  return struct.unpack("I", x)[0]

def r_until(st):
  ret = ""
  while st not in ret:
    r = s.recv(8192)
    if len(r) == 0:
      raise Exception("recv 0")
    ret += r
  return ret

def interact():
  t = telnetlib.Telnet()
  t.sock = s
  t.interact()

