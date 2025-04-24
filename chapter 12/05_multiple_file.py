with (open("file1.txt") as f1, open("file2.txt") as f2):
    text = f1.read()
    text2 =f2.read()

print(text)
print(text2)