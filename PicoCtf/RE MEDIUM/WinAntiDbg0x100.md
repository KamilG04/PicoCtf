#### Description

This challenge will introduce you to 'Anti-Debugging.' Malware developers don't like it when you attempt to debug their executable files because debugging these files reveals many of their secrets! That's why, they include a lot of code logic specifically designed to interfere with your debugging process. Now that you've understood the context, go ahead and debug this Windows executable! This challenge binary file is a Windows console application and you can start with running it using `cmd` on Windows. Challenge can be downloaded [here](https://artifacts.picoctf.net/c_titan/55/WinAntiDbg0x100.zip). Unzip the archive with the password `picoctf`

picoCtf/RE/WinAntiDbg0x100    
❯ file WinAntiDbg0x100.exe  
WinAntiDbg0x100.exe: PE32 executable for MS Windows 6.00 (console), Intel i386, 5 sections  
  
picoCtf/RE/WinAntiDbg0x100

wiec 32 

![[Pasted image 20260419132035.png]]

ctrl+g

F9 dochodzimy do breakpointa i w rejestrach widac ze 
![[Pasted image 20260419132644.png]]

## x32dbg skróty

| Klawisz    | Co robi                                                     |
| ---------- | ----------------------------------------------------------- |
| **F9**     | Run (leć do następnego breakpointa)                         |
| **F8**     | Step over (wykonaj jedną instrukcję, nie wchodź do funkcji) |
| **F7**     | Step into (wejdź do funkcji)                                |
| **F2**     | Postaw/usuń breakpoint na zaznaczonej linii                 |
| **Ctrl+G** | Idź pod adres / nazwę funkcji                               |
| **Ctrl+F** | Szukaj w kodzie                                             |
| **F4**     | Run to cursor (leć do miejsca gdzie stoi kursor)            |
Podmieniamy EAX na 0 mial 1 wiec latwo sie domyslec ze akurat w tym rejestrze 

![[Pasted image 20260419134418.png]]

I klasa flaga
