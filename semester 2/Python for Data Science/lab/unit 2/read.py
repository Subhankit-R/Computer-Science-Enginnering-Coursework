# READ entire file
with open("sample.txt", "r") as f:
    content = f.read()
    print("READ:\n", content)