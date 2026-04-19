Wiec 
import sys

def exit():
  sys.exit(0)

def scramble(L):
  A = L
  i = 2
  #Pop usuwa z pozycji element 
  while (i < len(A)):
    A[i-2] += A.pop(i-1)
    #append na koncu dodaje element 
    A[i-1].append(A[:i-2])
    i += 1

  return L

def get_flag():
  flag = open('flag.txt', 'r').read()
  flag = flag.strip()
  hex_flag = []
  for c in flag:
      #ord - int ascii
      #hex - int w hexa 
      #Hex oddaje stringa ale z prefixem 0x 
      #Tutaj ten str jest nie potrzebny 
    hex_flag.append([str(hex(ord(c)))])

  return hex_flag

def main():
  flag = get_flag()
  cypher = scramble(flag)
  print(cypher)

if __name__ == '__main__':
  main()

z netcata biore do pliku output tego hexa 
[['0x70', '0x69'], ['0x63', [], '0x6f'], ['0x43', [['0x70', '0x69']], '0x54'],

Rozne wielkosci to problem

def scramble(L):
  A = L
  i = 2
  #Pop usuwa z pozycji element 
  while (i < len(A)):
    A[i-2] += A.pop(i-1)
    #append na koncu dodaje element 
    A[i-1].append(A[:i-2])
    i += 1

  return L

Czyli aż i<len(A) zaczynamy od pierwszego elementu
I tutaj A.pop(i-1) usuwa element następny
A[i-2] przypisuje go na aktualna pozycje ?
A[i-1].append(A[:i-2]) 
Bierze element i-1 
i dodaje do niego fragment 
od poczatku do i-2 ? 
L = [[1], [2], [3], [4]]
A.pop(1) 2 znika
[[[[1,2], [3], [4]]]]
Tera ten append jebany
[3].append([])
append dodaje na koniec listy
wiec [[[[[[1,2],[3],[4]]],[3]]

No i fail no kolejka lifo // bfs 
dawno sie takich rzeczy nie robilo, ale lifehack na ctf:


EEEEE 
tutaj jest schemat 
doslownie wywalenie list zagniezdzonych bo sa smieciami i to tyle
strings = [x for x in elem if isinstance(x, str)] 

strings = []
for x in elem:
    if isinstance(x, str):
        strings.append(x)
```

`isinstance(x, str)` — sprawdza czy `x` jest stringiem (a nie listą).

i to dziala XD 





