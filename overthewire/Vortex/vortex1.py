from pwn import *

def pwn():
    r = remote('vortex.labs.overthewire.org', 5842)
    a = r.recv(4)
    b = r.recv(4)
    c = r.recv(4)
    d = r.recv(4)
    a = struct.unpack('<I', a)[0]
    b = struct.unpack('<I', b)[0]
    c = struct.unpack('<I', c)[0]
    d = struct.unpack('<I', d)[0]
    e = a+b+c+d
    e = struct.pack('I', e)
    r.sendline(str(e))
    
    r.interactive()

pwn()
