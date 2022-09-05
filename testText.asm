JMP
HERE 4
HERE 0 , global value (i)
HERE 0 , temporary global value
LDIA 0 , load small integer
STA 2 , store value in variable 'i'
JMP
HERE 12
AIN 2 , load variable 'i'
LDIB 1
ADD , increment value
STA 2 , store value in variable 'i'
AIN 2 , load variable 'i'
LDIB 36 , load small integer
SUB , operator <
JMPZ
HERE 37
JMPC
HERE 37
JMP
HERE 21
LDW
HERE 61294 , load large integer
SWP
AIN 2 , load variable 'i'
ADD , add to pointer address
STA 3
LDIA 41
SWP
AIN 2 , load variable 'i'
ADD , add to pointer address
LDAIN
BIN 3
SWP
STAOUT , store value in array
JMP
HERE 8 , jump to next iteration
JMP
HERE 4
JMP
HERE 77
HERE 13 , string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
HERE 14
HERE 15
HERE 16
HERE 17
HERE 18
HERE 19
HERE 20
HERE 21
HERE 22
HERE 23
HERE 24
HERE 25
HERE 26
HERE 27
HERE 28
HERE 29
HERE 30
HERE 31
HERE 32
HERE 33
HERE 34
HERE 35
HERE 36
HERE 37
HERE 38
HERE 39
HERE 40
HERE 41
HERE 42
HERE 43
HERE 44
HERE 45
HERE 46
HERE 47
HERE 48
