RST
STM #0 // 0 int, 1 mem, 2 REG
STA #77
STB #8
ADD
STM #2 // register mode
STX @C

STM #0
b #17 // a 17ös sorra ugrik
STY #1 // eq
b #17
STY #2 // Less Than
b #17
STY #3 // greater then

CMP
BEQ #11 // a = b
BLT #13 // a > b
BGT #15 // a < b