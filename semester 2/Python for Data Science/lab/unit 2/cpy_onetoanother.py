# COPY from one file to another
with open("sample.txt", "r") as src:
    data = src.read()

with open("copy.txt", "w") as dst:
    dst.write(data)
print("File copied to copy.txt")