def polindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return polindrom(s[1:-1])

print(polindrom('walaw'))