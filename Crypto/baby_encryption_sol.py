f = open("q.txt","r")
for line in f:
    b = bytes.fromhex(line) #convert hex strings to byte strings for XORing
    for k in range(255):
        d = bytes([char ^ k for char in b])
        if b'd4rkc0de' in d:
            print(d)