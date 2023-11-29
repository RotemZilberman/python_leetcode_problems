def isValid(s):
    count = 0
    for string in s.split('.'):
        count += 1
        if not string.isdigit() or (string[0] == '0' and len(string) > 1):
            return False
        num = int(string)
        if num < 0 or num > 255:
            return False
    if count != 4:
        return False
    return True
S = "0.0.0.0"
print(isValid(S))