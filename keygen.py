from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Generate private key
private_key = ec.generate_private_key(ec.SECP256R1())

# Convert private key to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption(),
)

# Generate public key
public_key = private_key.public_key()

# Convert public key to PEM format
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

# Save keys to files
with open("private_key.pem", "wb") as f:
    f.write(private_pem)

with open("public_key.pem", "wb") as f:
    f.write(public_pem)

print("✅ Keys generated and saved!")
