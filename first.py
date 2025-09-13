str = input("Enter a string: ")
rev_str = ""
index = len(str) - 1
while index >= 0:
    rev_str = rev_str + str[index]
    index = index - 1
print("Reversed string:", rev_str)