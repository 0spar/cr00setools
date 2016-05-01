import socket

s = socket.create_connection(("127.0.0.1", 3002))

def r_until(st):
  ret = ""
  while st not in ret:
    s.recv(8192)


