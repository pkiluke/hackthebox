input_b = bytes.fromhex("134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9")
flag_format = str.encode('HTB{')

# key = ''.join([chr(flag_format[i] ^ input_b[i]) for i in range(0, 4)])
key = [flag_format[i] ^ input_b[i] for i in range(0, 4)]


def decrypt(data: bytes) -> bytes:
    xored = b''
    for i in range(len(input_b)):
        xored += bytes([input_b[i] ^ key[i % len(key)]])
    return xored


print(decrypt(input_b))
