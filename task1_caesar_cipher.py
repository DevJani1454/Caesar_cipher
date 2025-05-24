def apply_cipher(text, key, mode):
    result = []
    for char in text:
        if char.isupper():
            base = ord('A')
            shifted = (ord(char) - base + key * mode) % 26
            result.append(chr(shifted + base))
        elif char.islower():
            base = ord('a')
            shifted = (ord(char) - base + key * mode) % 26
            result.append(chr(shifted + base))
        else:
            result.append(char)
    return ''.join(result)

def brute_force_decryption(ciphertext):
    print("\n🔍 Brute-force decryption initiated")
    print("Testing all possible keys (1-25):")
    print("--------------------------------")
    
    for key in range(1, 26):
        decrypted = apply_cipher(ciphertext, key, -1)
        print(f"Key {key:2d}: {decrypted}")
    
    print("\nThe correct decryption will appear as readable text")

def display_interface():
    print("\n🔐 Cryptographic Message Tool 🔐")
    print("Caesar Cipher Encryption/Decryption System")
    print("\nOptions:")
    print("1. Encrypt plaintext")
    print("2. Decrypt ciphertext (known key)")
    print("3. Decrypt ciphertext (unknown key)")
    print("4. Exit")

def execute_program():
    while True:
        display_interface()
        choice = input("Select operation (1-4): ")
        
        if choice == '1':
            plaintext = input("Enter plaintext to encrypt: ")
            encryption_key = int(input("Enter encryption key (1-25): "))
            ciphertext = apply_cipher(plaintext, encryption_key, 1)
            print(f"\nEncrypted message: {ciphertext}")
        
        elif choice == '2':
            ciphertext = input("Enter ciphertext to decrypt: ")
            decryption_key = int(input("Enter decryption key: "))
            plaintext = apply_cipher(ciphertext, decryption_key, -1)
            print(f"\nDecrypted message: {plaintext}")
        
        elif choice == '3':
            ciphertext = input("Enter ciphertext for brute-force decryption: ")
            brute_force_decryption(ciphertext)
        
        elif choice == '4':
            print("\nTerminating cryptographic operations. Goodbye!")
            return
        
        else:
            print("Invalid selection. Please choose 1-4")

if __name__ == "__main__":
    execute_program()