from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization

# Load Private Key
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(), password=None
    )

# Load Public Key
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read()
    )

# Transaction Data (Can be any message)
transaction_data = "UserA sends 10 tokens to UserB".encode()

# Sign the Transaction
signature = private_key.sign(
    transaction_data,
    ec.ECDSA(hashes.SHA256())
)

print("✅ Transaction Signed!")
print(f"Signature: {signature.hex()}")

# Verify the Signature
try:
    public_key.verify(
        signature,
        transaction_data,
        ec.ECDSA(hashes.SHA256())
    )
    print("✅ Signature Verified! Transaction is authentic.")
except:
    print("❌ Signature Verification Failed! Transaction is invalid.")
