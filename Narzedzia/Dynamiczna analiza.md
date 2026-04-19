LLDB 
Ściągawka 
lldb ./binary
```

### Breakpointy
```
breakpoint set -n funkcja          # po nazwie (symbol z binarki)
breakpoint set -a 0xADRES          # po adresie (offset gdy brak PIE)
breakpoint list                    # lista breakpointów
breakpoint delete 1                # usuń breakpoint #1
```

### Uruchamianie
```
process launch                     # uruchom normalnie
process launch --stop-at-entry     # zatrzymaj na samym starcie
process launch -- arg1 arg2        # z argumentami
run                                # skrót
```

### Kontrola wykonania
```
continue / c                       # kontynuuj do następnego BP
finish                             # wykonaj do końca funkcji (step out)
next / n                           # następna linia (step over)
step / s                           # wejdź do funkcji (step into)
```

### Inspekcja pamięci i rejestrów
```
register read                      # wszystkie rejestry
register read rdi rsi rax          # konkretne rejestry
x/s $rdi                           # string pod adresem z rdi
x/s 0xADRES                        # string pod konkretnym adresem
x/8gx $rsp                         # 8 qwordów ze stosu (hex)
x/20wx $rsp                        # 20 dwordów ze stosu
```

### Disasemblacja
```
disassemble -n main                # disas funkcji main
disassemble -s 0x1333 -e 0x13c4   # disas zakresu adresów
disassemble -f                     # disas aktualnej ramki
```

### Informacje o binarce
```
image list                         # załadowane moduły + base adresy
image dump symtab binary           # tablica symboli
image lookup -n funkcja            # szukaj symbolu
```

### Misc
```
kill                               # zabij proces
quit / q                           # wyjdź z LLDB
help komenda                       # pomoc
```

---

### Kolejność na RE challenge
```
1. image dump symtab    → co jest w binarce
2. breakpoint na ciekawą funkcję (decode, check, verify)
3. process launch --stop-at-entry → potem BP na strcmp/libc
4. finish → x/s $rdi / x/s $rsi

Win32
| Klawisz    | Co robi                                                     |
| ---------- | ----------------------------------------------------------- |
| **F9**     | Run (leć do następnego breakpointa)                         |
| **F8**     | Step over (wykonaj jedną instrukcję, nie wchodź do funkcji) |
| **F7**     | Step into (wejdź do funkcji)                                |
| **F2**     | Postaw/usuń breakpoint na zaznaczonej linii                 |
| **Ctrl+G** | Idź pod adres / nazwę funkcji                               |
| **Ctrl+F** | Szukaj w kodzie                                             |
| **F4**     | Run to cursor (leć do miejsca gdzie stoi kursor)            |
