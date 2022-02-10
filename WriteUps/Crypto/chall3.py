from Crypto.Cipher import AES
import os
import sys

KEY = os.urandom(16) #unknown 16 byte key
with open('flag.txt', 'rb') as f:
    FLAG = f.read()
menu = """1. Give plaintext to encrypt
2. Check my ciphertext
3. Retrieve the flag
4. Exit"""

def encrypt():
    text=input("give your plaintext in hex : ")
    plaintext = bytes.fromhex(text)
    if len(plaintext) % 16 != 0:
        return {"error": "Data length must be multiple of 16"}

    cipher = AES.new(KEY, AES.MODE_CBC, KEY)
    encrypted = cipher.encrypt(plaintext)

    print("ciphertext : ",encrypted.hex())
    sys.stdout.flush()



def get_flag():
    key=input("give key in hex : ")
    key = bytes.fromhex(key)

    if key == KEY:
        print(FLAG)
        sys.exit("Congrats n00b..")
    else:
        print("Wrong key")
        sys.stdout.flush()


def receive():
    text=input("give your ciphertext in hex : ")
    ciphertext = bytes.fromhex(text)
    if len(ciphertext) % 16 != 0:
        print("Data length must be multiple of 16")
        sys.stdout.flush()

        return None

    cipher = AES.new(KEY, AES.MODE_CBC, KEY)
    decrypted = cipher.decrypt(ciphertext)

    try:
        decrypted.decode() # ensure plaintext is valid ascii
    except UnicodeDecodeError:
        print("Invalid plaintext: ",decrypted.hex())
        sys.stdout.flush()
        
        return None

    print("success ! Your message has been received")
    sys.stdout.flush()


def main():
    while(True):
        print(menu)
        sys.stdout.flush()

        value=input("Enter your choice : ")
        if value == "1":
            encrypt()
        elif value == "2":
            receive()
        elif value == "3":
            get_flag()
        else:
            sys.exit("Good bye..")

if __name__ == "__main__":
    main()
