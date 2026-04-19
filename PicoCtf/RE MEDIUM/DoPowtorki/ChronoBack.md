picoCTF{UseSecure#$_Random@j3n3r@T0rs223d724e}
import random import time from pwn import * def get_random(length,seed): alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" random.seed(seed) # seeding with current time s = "" for i in range(length): s += random.choice(alphabet) return s def main(): print("Welcome to the token generation challenge!") token_length = 20 # the token length offset=0 while (1): seed = int(time.time()*1000+offset) r=remote("verbal-sleep.picoctf.net", 62036) token = get_random(token_length,seed) n=0 while n != 50: try: user_guess = r.recvuntil(b"Enter your guess for the token (or exit):") r.sendline(token) print(offset,n,token) ans=(r.recvline()) if b"Congratulations" in ans: print(ans) ans=(r.recvline()) print(ans) return print(ans) seed = seed+1 token = get_random(token_length,seed) n+=1 except KeyboardInterrupt: print("\nKeyboard interrupt detected. Exiting the program...") offset=offset+40 if _name_ == "__main__": main()


#!/usr/bin/env python3
import random
import time
from pwn import *

context.log_level = 'error'  

HOST = "verbal-sleep.picoctf.net"
PORT = 61098

def get_token(seed):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(seed)
    return ''.join(random.choice(alphabet) for _ in range(20))

for attempt in range(10000):
    t0 = int(time.time() * 1000)
    try:
        io = remote(HOST, PORT)
        io.recvuntil(b"(or exit):", timeout=5)
        
        # seed był ustawiony tuż przed wydrukiem bannera
        # próbuj t0, t0-1, t0+1, t0-2, t0+2 ... w jednym połączeniu
        base = t0
        tokens = [get_token(base + d) for d in [0,-1,1,-2,2,-3,3,-4,4,-5,
                                                  5,-6,6,-7,7,-8,8,-9,9,-10,
                                                  10,-15,15,-20,20,-30,30,-50,
                                                  50,-75,75,-100,100,-150,150,
                                                  -200,200,-300,300,-400,400,
                                                  -500,500,-750,750,-1000,1000,
                                                  -1500,1500]]
        
        for token in tokens[:49]:
            io.sendline(token.encode())
        
        resp = io.recvrepeat(2)
        io.close()
        
        if b"Congratulations" in resp or b"picoCTF" in resp:
            print("[+] FLAG:")
            print(resp.decode())
            break
            
        if attempt % 10 == 0:
            print(f"[*] attempt {attempt}, t0={t0}")
            
    except Exception as e:
        print(f"[-] Error: {e}")
        time.sleep(0.5)
(venv) zimmermann@zimmermann ~/D/p/R/TokenGeneration> 

