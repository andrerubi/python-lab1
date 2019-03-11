string = input("Insert a string: ")
str_len = len(string)

if str_len < 2:
    new_str = ""
else:
    new_str = string[0] + string[1] + string[str_len-2] + string[str_len-1]

print(new_str)
