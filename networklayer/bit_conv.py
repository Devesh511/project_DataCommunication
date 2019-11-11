def str2bits(string):
    res = ""
    for x in string:
        bits = ''.join(format(ord(x), 'b'))
        while len(bits) != 8:
            bits = '0' + bits
        res += str(bits)
    return res


def bits2str(string):
    res = ""
    for i in range(0, len(string), 8):
        j = min(i+8, len(string))
        char = chr(int(string[i:j], 2))
        res += char
    return res