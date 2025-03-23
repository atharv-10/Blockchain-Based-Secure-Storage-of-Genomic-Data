from blockchain import encrypt  # Import the encryption function

test_data = "Block from Node 1"
try:
    encrypted_data = encrypt(test_data)
    print("Encryption Successful:", encrypted_data)
except Exception as e:
    print("Encryption Failed:", e)
