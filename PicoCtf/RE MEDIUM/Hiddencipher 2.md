What is 8 - 0? 8
Encoded flag values:
896, 840, 792, 888, 536, 672, 560, 984, 816, 776, 856, 808, 760, 816, 864, 776, 824, 1000
(venv) zimmermann@zimmermann ~/D/p/R/Hidden Cipher 2> 

![[Pasted image 20260328155117.png]]

Po ogarnieciu tego rename retype itd 

![[Pasted image 20260328162606.png]]

Tak samo
Te ulong w printfie to artefakty kompilacji bo sa argumentami funkcji rozszerzane do 64 bitow przed wrzuceniem na stos/rejestr wiec ghidra daje to jak casty 

![[Pasted image 20260328163001.png]]

To wyglada jak zwykle wczytanie pliku w C ale dla rozgrzewki

![[Pasted image 20260328163057.png]]
![[Pasted image 20260328164942.png]]

![[Pasted image 20260328170457.png]]

