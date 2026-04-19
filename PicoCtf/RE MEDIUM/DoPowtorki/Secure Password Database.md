
## Opis zadania

> "I made a new password authentication program that even shows you the password you entered saved in the database! Isn't that cool?"

Załącznik: `system.out` 

---



````python
data = [105, 85, 98, 104, 56, 49, 33, 106, 42, 104, 110, 33]

h = 0x1505
for b in data:
    h = (b + h * 0x21) & 0xFFFFFFFFFFFFFFFF

print(h)  # 15237662580160011234
```

---

### Flaga
```
picoCTF{d0nt_trust_us3rs}
````

