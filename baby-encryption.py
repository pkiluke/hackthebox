# encryption function
def encryption(c):
    # modulo = can't reverse engineer
    return (123 * c + 18) % 256


f = open('/Users/pkiluke/hackthebox/baby-encryption/msg.enc')
msg = bytes.fromhex(f.read())

# create a dictionary = key:value = encrypted character:corresponding plaintext ASCII character
# (0,128) = basic ASCII table; https://www.asciitable.com
map_a = {encryption(x): x for x in range(0, 128)}
# create a list = dynamically sized array
print(''.join([chr(map_a[char]) for char in msg]))
