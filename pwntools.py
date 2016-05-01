import time
from pwn import *
import struct
from hexdump import hexdump


def q(x):
  return struct.pack("I", x)

def Q(x):
  return struct.unpack("I", x)[0]

r = remote('127.0.0.1', 4000)
#r.recvuntil(">")
#r.interactive()

