Solution to shellcode 
==================
#First Step
利用IDA pro反編譯後，觀察程式碼，可以發現strcpy會發生overflow。
透過gdb和pwntools cyclic計算出offset。
但是，buffer太小，不能直接塞shellcode，只好讓main return指向read，
	stack順序為
	read address
	return address
	agrv[0] 0
	agrv[1] the address for read to write
	argv[2] length of read, it doesn't matter


