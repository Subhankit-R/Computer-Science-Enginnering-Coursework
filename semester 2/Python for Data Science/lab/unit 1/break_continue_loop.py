# Loop with break and continue
for i in range(10):
    if i == 7:
        break
    if i % 2 == 0:
        continue
    print(i)   # Prints odd numbers until 7