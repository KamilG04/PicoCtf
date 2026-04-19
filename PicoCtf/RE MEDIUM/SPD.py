secret = [105, 85, 98, 104, 56, 49, 33, 106, 42, 104, 110, 33]

h = 5381
for c in secret:
    h = (h * 33 + c) & 0xffffffffffffffff

print(h)
