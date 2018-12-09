from pwn import *

r = remote('pwnable.kr', 9007)
def locloc():
	ifthis = """N=(\d+) C=(\d+)"""

        NandC  =  r.recvline_regex(ifthis)
        result =  re.search(ifthis, NandC)
        N, C   =  result.groups()
        N      =  int(N)
        C      =  int(C)
	return N, C

def pwn():
    round=0
    r.recvuntil("Ready?")
    while True:
	round+=1
	log.info("Round: "+str(round))
        N, C = locloc()
        begin = 0
        end   = N-1
        for i in xrange(C):
            middle = (begin+end)/2
            coins = []
            for i in range(begin, middle+1):
                coins.append(str(i))
            test = " ".join(coins)
            r.sendline(test)
            resp     = """(\d+)"""
            rec      = r.recvline()
            lol      = re.search(resp, rec)
            thereare = int(lol.groups()[0])
            shouldbe = len(coins)*10
            thereare = int(thereare)
            if thereare == shouldbe:
                begin = middle+1
                end = end
            else:
                begin = begin
                end = middle

        r.sendline(str(begin))


pwn()
