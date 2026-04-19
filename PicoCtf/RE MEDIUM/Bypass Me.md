#### Description

Your task is to analyze and exploit a password-protected binary called **bypassme.bin** and binary performs input sanitization. However, instead of guessing the password, you are expected to reverse engineer or debug the program to bypass the authentication logic and retrieve the hidden flag. You'll need to think like an attacker using tool like [LLDB](https://lldb.llvm.org/use/tutorial.html) to uncover how the binary works under the hood and leak the correct password.

Additional details will be available after launching your challenge instance.


1.ssh ctf-player@foggy-cliff.picoctf.net -p 52455

![[Pasted image 20260328130342.png]]

2.image dump symtab bypassme.bin
Symtab, file = /home/ctf-player/bypassme.bin, num_symbols = 100:
               Debug symbol
               |Synthetic symbol
               ||Externally Visible
               |||
Index   UserID DSX Type            File Address/Value Load Address       Size               Flags      Name
------- ------ --- --------------- ------------------ ------------------ ------------------ ---------- ----------------------------------
[    0]      1     Invalid         0x0000000000000318                    0x000000000000001c 0x00000003 
[    1]      2     Invalid         0x0000000000000338                    0x0000000000000020 0x00000003 
[    2]      3     Invalid         0x0000000000000358                    0x0000000000000024 0x00000003 
[    3]      4     Invalid         0x000000000000037c                    0x0000000000000020 0x00000003 
[    4]      5     Invalid         0x00000000000003a0                    0x0000000000000030 0x00000003 
[    5]      6     Invalid         0x00000000000003d0                    0x00000000000001f8 0x00000003 
[    6]      7     Invalid         0x00000000000005c8                    0x00000000000000f1 0x00000003 
[    7]      8     Invalid         0x00000000000006ba                    0x000000000000002a 0x00000003 
[    8]      9     Invalid         0x00000000000006e8                    0x0000000000000030 0x00000003 
[    9]     10     Invalid         0x0000000000000718                    0x00000000000000f0 0x00000003 
[   10]     11     Invalid         0x0000000000000808                    0x0000000000000138 0x00000003 
[   11]     12     Invalid         0x0000000000001000                    0x000000000000001b 0x00000003 
[   12]     13     Invalid         0x0000000000001020                    0x0000000000000010 0x00000003 
[   13]     14     Invalid         0x0000000000001100                    0x0000000000000010 0x00000003 
[   14]     15     Invalid         0xscp -P 52455 ctf-player@foggy-cliff.picoctf.net:bypassme.bin .
0000000000001110                    0x00000000000000d0 0x00000003 
[   15]     16     Invalid         0x00000000000011e0                    0x0000000000000030 0x00000003 
[   16]     17     Invalid         0x00000000000018b8                    0x000000000000000d 0x00000003 
[   17]     18     Invalid         0x0000000000002000                    0x00000000000008a0 0x00000003 
[   18]     19     Invalid         0x00000000000028a0                    0x000000000000006c 0x00000003 
[   19]     20     Invalid         0x0000000000002910                    0x00000000000001a4 0x00000003 
[   20]     21     Invalid         0x0000000000003d58                    0x0000000000000008 0x00000003 
[   21]     22     Invalid         0x0000000000003d60                    0x0000000000000008 0x00000003 
[   22]     23     Invalid         0x0000000000003d68                    0x00000000000001f0 0x00000003 
[   23]     24     Invalid         0x0000000000003f58                    0x00000000000000a8 0x00000003 
[   24]     25     Invalid         0x0000000000004000                    0x0000000000000008 0x00000003 
[   25]     26     Invalid         0x0000000000004010                    0x0000000000000010 0x00000003 
[   26]     27     Invalid         0x0000000000000000                    0x0000000000000318 0x00000003 
[   27]     28     Invalid         0x0000000000000000                    0x0000000000000318 0x00000003 
[   28]     29     Invalid         0x0000000000000000                    0x0000000000000318 0x00000003 
[   29]     30     Invalid         0x0000000000000000                    0x0000000000000318 0x00000003 
[   30]     31     Invalid         0x0000000000000000                    0x0000000000000318 0x00000003 
[   31]     32     Invalid         0x0000000000000000                    0x0000000000000318 0x00000003 
[   32]     33     SourceFile      0x0000000000000000                    0x0000000000000000 0x00000004 crtstuff.c
[   33]     34     Code            0x0000000000001210                    0x0000000000000030 0x00000002 deregister_tm_clones
[   34]     35     Code            0x0000000000001240                    0x0000000000000040 0x00000002 register_tm_clones
[   35]     36     Code            0x0000000000001280                    0x0000000000000040 0x00000002 __do_global_dtors_aux
[   36]     37     Data            0x0000000000004028                    0x0000000000000001 0x00000001 completed.8061
[   37]     38     Data            0x0000000000003d60                    0x0000000000000008 0x00000001 __do_global_dtors_aux_fini_array_entry
[   38]     39     Code            0x00000000000012c0                    0x0000000000000009 0x00000002 frame_dummy
[   39]     40     Data            0x0000000000003d58                    0x0000000000000008 0x00000001 __frame_dummy_init_array_entry
[   40]     41     SourceFile      0x0000000000000000                    0x0000000000000000 0x00000004 bypassme.c
[   41]     42     SourceFile      0x0000000000000000                    0x0000000000000000 0x00000004 crtstuff.c
[   42]     43     Data            0x0000000000002ab4                    0x0000000000000004 0x00000001 __FRAME_END__
[   43]     45     Invalid         0x0000000000003d60                    0x0000000000000008 0x00000000 __init_array_end
[   44]     46     Data            0x0000000000003d68                    0x00000000000001f0 0x00000001 _DYNAMIC
[   45]     47     Invalid         0x0000000000003d58                    0x0000000000000008 0x00000000 __init_array_start
[   46]     48     Invalid         0x00000000000028a0                    0x000000000000006c 0x00000000 __GNU_EH_FRAME_HDR
[   47]     49     Data            0x0000000000003f58                    0x00000000000000a8 0x00000001 _GLOBAL_OFFSET_TABLE_
[   48]     50     Code            0x0000000000001000                    0x000000000000001b 0x00000002 _init
[   49]     51   X Code            0x00000000000018b0                    0x0000000000000005 0x00000012 __libc_csu_fini
[   50]     52   X Undefined       0x0000000000000000                    0x0000000000000000 0x00000012 putchar@@GLIBC_2.2.5
[   51]     53     Undefined       0x0000000000000000                    0x0000000000000000 0x00000020 _ITM_deregisterTMCloneTable
[   52]     54   X Data            0x0000000000004010                    0x0000000000000008 0x00000011 stdout@@GLIBC_2.2.5
[   53]     55     Data            0x0000000000004000                    0x0000000000000008 0x00000020 data_start
[   54]     56   X Undefined       0x0000000000000000                    0x0000000000000000 0x00000012 puts@@GLIBC_2.2.5
[   55]     57   X Data            0x0000000000004020                    0x0000000000000008 0x00000011 stdin@@GLIBC_2.2.5
[   56]     58   X Data            0x0000000000004010                    0x0000000000000010 0x00000010 _edata
[   57]     59   X Undefined       0x0000000000000000                    0x0000000000000000 0x00000012 fclose@@GLIBC_2.2.5
[   58]     60   X Code            0x00000000000018b8                    0x000000000000000d 0x00000212 _fini
[   59]     61   X Undefined       0x0000000000000000                    0x0000000000000000 0x00000012 __stack_chk_fail@@GLIBC_2.4
[   60]     62   X Undefined       0x0000000000000000                    0x0000000000000000 0x00000012 printf@@GLIBC_2.2.5
[   61]     63   X Undefined       0x0000000000000000                    0x0000000000000000 0x00000012 strcspn@@GLIBC_2.2.5
[   62]     64   X Undefined       0x0000000000000000                    0x0000000000000000 0x00000012 __libc_start_main@@GLIBC_2.2.5
[   63]     65   X Undefined       0x0000000000000000                    0x0000000000000000 0x00000012 fgets@@GLIBC_2.2.5
[   64]     66   X Data            0x0000000000004000                    0x0000000000000008 0x00000010 __data_start
[   65]     67   X Undefined       0x0000000000000000                    0x0000000000000000 0x00000012 strcmp@@GLIBC_2.2.5
[   66]     68     Undefined       0x0000000000000000                    0x0000000000000000 0x00000020 __gmon_start__
[   67]     69   X Data            0x0000000000004008                    0x0000000000000008 0x00000211 __dso_handle
[   68]     70   X Data            0x0000000000002000                    0x0000000000000004 0x00000011 _IO_stdin_used
[   69]     71   X Code            0x00000000000013c4                    0x0000000000000093 0x00000012 sanitize(char const*, char*)
[   70]     72   X Code            0x0000000000001840                    0x0000000000000065 0x00000012 __libc_csu_init
[   71]     73   X Undefined       0x0000000000000000                    0x0000000000000000 0x00000012 fflush@@GLIBC_2.2.5
[   72]     74   X Data            0x0000000000004030                    0x0000000000000000 0x00000010 _end
[   73]     75   X Code            0x00000000000011e0                    0x000000000000002f 0x00000012 _start
[   74]     76   X Undefined       0x0000000000000000                    0x0000000000000000 0x00000012 isalpha@@GLIBC_2.2.5
[   75]     77   X Data            0x0000000000004010                    0x0000000000000010 0x00000010 __bss_start
[   76]     78   X Code            0x000000000000162e                    0x000000000000020b 0x00000012 main
[   77]     79   X Undefined       0x0000000000000000                    0x0000000000000000 0x00000012 fopen@@GLIBC_2.2.5
[   78]     80   X Code            0x0000000000001457                    0x000000000000006f 0x00000012 auth_sequence()
[   79]     81   X Code            0x0000000000001333                    0x0000000000000091 0x00000012 decode_password(char*)
[   80]     82   X Code            0x00000000000012c9                    0x000000000000006a 0x00000012 type_out(char const*, unsigned int)
[   81]     83   X Data            0x0000000000004010                    0x0000000000000010 0x00000211 __TMC_END__
[   82]     84   X Code            0x00000000000014c6                    0x0000000000000168 0x00000012 intro_sequence()
[   83]     85     Undefined       0x0000000000000000                    0x0000000000000000 0x00000020 _ITM_registerTMCloneTable
[   84]     86   X Undefined       0x0000000000000000                    0x0000000000000000 0x00000012 sleep@@GLIBC_2.2.5
[   85]     87     Undefined       0x0000000000000000                    0x0000000000000000 0x00000022 __cxa_finalize@@GLIBC_2.2.5
[   86]     88   X Undefined       0x0000000000000000                    0x0000000000000000 0x00000012 usleep@@GLIBC_2.2.5
[   87]     89  S  Trampoline      0x0000000000001030                    0x0000000000000010 0x00000000 putchar
[   88]     90  S  Trampoline      0x0000000000001040                    0x0000000000000010 0x00000000 puts
[   89]     91  S  Trampoline      0x0000000000001050                    0x0000000000000010 0x00000000 fclose
[   90]     92  S  Trampoline      0x0000000000001060                    0x0000000000000010 0x00000000 __stack_chk_fail
[   91]     93  S  Trampoline      0x0000000000001070                    0x0000000000000010 0x00000000 printf
[   92]     94  S  Trampoline      0x0000000000001080                    0x0000000000000010 0x00000000 strcspn
[   93]     95  S  Trampoline      0x0000000000001090                    0x0000000000000010 0x00000000 fgets
[   94]     96  S  Trampoline      0x00000000000010a0                    0x0000000000000010 0x00000000 strcmp
[   95]     97  S  Trampoline      0x00000000000010b0                    0x0000000000000010 0x00000000 fflush
[   96]     98  S  Trampoline      0x00000000000010c0                    0x0000000000000010 0x00000000 isalpha
[   97]     99  S  Trampoline      0x00000000000010d0                    0x0000000000000010 0x00000000 fopen
[   98]    100  S  Trampoline      0x00000000000010e0                    0x0000000000000010 0x00000000 sleep
[   99]    101  S  Trampoline      0x00000000000010f0                    0x0000000000000010 0x00000000 usleep
(lldb) breakpoint set -n strcmp
Breakpoint 1: no locations (pending).
WARNING:  Unable to resolve breakpoint to any actual locations.
(lldb) breakpoint set -a 0x10a0
Breakpoint 2: address = 0x00000000000010a0
(lldb) process launch
Process 103 launched: '/home/ctf-player/bypassme.bin' (x86_64)
kill

[1]+  Stopped                 lldb ./bypassme.bin

ctf-player@pico-chall$ ^C
ctf-player@pico-chall$ lldb ./bypassme.bin
(lldb) target create "./bypassme.bin"
Current executable set to '/home/ctf-player/bypassme.bin' (x86_64).
(lldb) breakpoint delete 1
error: No breakpoints exist to be deleted.
(lldb) breakpoint set -n decode_password
Breakpoint 1: where = bypassme.bin`decode_password(char*) + 31 at bypassme.c:17:19, address = 0x0000000000001352
(lldb) process launch
Process 125 launched: '/home/ctf-player/bypassme.bin' (x86_64)
Process 125 stopped
* thread #1, name = 'bypassme.bin', stop reason = breakpoint 1.1
    frame #0: 0x000060bf7f686352 bypassme.bin`decode_password(out="\x98\x9c\xb7��\x7f") at bypassme.c:17:19
(lldb) finish
Process 125 stopped
* thread #1, name = 'bypassme.bin', stop reason = step out

    frame #0: 0x000060bf7f686665 bypassme.bin`main at bypassme.c:80:19
(lldb) x/s $rax
error: failed to read memory from 0x0.
(lldb) x/s $rdi
0x7ffec6b79c90: "SuperSecure"
(lldb) x/s $rsi
0x7ffec6b79e98: "\x19\xffffffae\xffffffb7\xffffffc6\xfffffffe\x7f"
(lldb) quit

Na x86-64 argumenty o ile nie sa w stosie to są w rejestrach 
argument 1  →  rdi
argument 2  →  rsi
argument 3  →  rdx
argument 4  →  rcx
argument 5  →  r8
argument 6  →  r9
return →  rax

Próba strcmp nie zadziałała bo przecież strcmp jest SO dynamicznie linkowane.

breakpoint set -a 0x10a0
Czyli adres strcmp też nie zadziałał bo PIE 
breakpoint set -n decode_password
zadziałał

Ogółem plik można było pobrać przez SCP
scp -P 52455 ctf-player@foggy-cliff.picoctf.net:bypassme.bin .
![[Pasted image 20260328132227.png]]


Dosyć prosto też byłoby usunąć weryfikację hasła
![[Pasted image 20260328135120.png]]![[Pasted image 20260328135618.png]]
ale wiadomo flaga siedzi w root