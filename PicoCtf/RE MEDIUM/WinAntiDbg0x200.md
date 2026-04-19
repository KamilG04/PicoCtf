Wogole pierwszy check to sprawdzenie czy korzystamy z debuggera xD

![[Pasted image 20260419153550.png]]

Ogolem 
1: [esp] 00115E1E 00115E1E "picoCTF{0x200_debug_f0r_Win_3fa9b221}"

z tego co wiem IsDebuggerPresent 
EAX = 1 jak jest debugger i EAX = 0 jak nie ma
Potem jest if wiec je ale wystarczy to spatchowac na jne i essa klasyczny manewr 
```
cVar1 = FUN_004011d0()
if (cVar1 == '\0') {
```
to tworzy nowy proces i sprawdza jw.
0040181c  e8 af f9        CALL       FUN_004011d0
00401821  0f b6 d0        MOVZX      EDX,AL
00401824  85 d2           TEST       EDX,EDX
00401826  75 0a           JNZ        LAB_00401832
tam jeszcze xoruje flage ogolem najlatwiej to spatchowac jak nie to dolaczyc proces
![[Pasted image 20260419154537.png]]