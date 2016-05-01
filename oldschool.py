import socket
import telnetlib

s = socket.create_connection(("127.0.0.1", 4000))

def r_until(st):
  ret = ""
  while st not in ret:
    s.recv(8192)

def interact():
  t = telnetlib.Telnet()
  t.sock = s
  t.interact()

