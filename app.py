from flask import Flask, request, jsonify, render_template_string
import hashlib
import time
import json
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# 🔥 Initialize Flask
app = Flask(__name__)

# 🔒 AES-256 Encryption Setup
AES_KEY = os.urandom(32)  # 256-bit key
AES_IV = os.urandom(16)   # 16-byte IV

def encrypt_data(data):
    """Encrypts genomic data using AES-256."""
    cipher = Cipher(algorithms.AES(AES_KEY), modes.CBC(AES_IV), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad data to 16 bytes (AES block size)
    padded_data = data.ljust(16 * ((len(data) // 16) + 1))
    
    return encryptor.update(padded_data.encode()) + encryptor.finalize()

def decrypt_data(encrypted_data):
    """Decrypts AES-encrypted genomic data."""
    cipher = Cipher(algorithms.AES(AES_KEY), modes.CBC(AES_IV), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_data).decode().strip()

# 🧱 Block Class
class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Generates SHA-256 hash of the block."""
        block_string = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "data": self.data
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

# ⛓ Blockchain Class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """Creates the first block (Genesis Block)."""
        return Block(0, "0", encrypt_data("Genesis Block").hex())

    def add_block(self, data):
        """Adds a new encrypted block to the chain."""
        encrypted_data = encrypt_data(data).hex()
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), last_block.hash, encrypted_data)
        self.chain.append(new_block)
        return new_block

    def get_chain(self):
        """Returns the blockchain with decrypted data."""
        return [{
            "index": block.index,
            "previous_hash": block.previous_hash,
            "timestamp": block.timestamp,
            "data": decrypt_data(bytes.fromhex(block.data)),  # Decrypt data
            "hash": block.hash
        } for block in self.chain]

# 🚀 Initialize Blockchain
blockchain = Blockchain()

# 🌐 Web UI for Input
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Blockchain Data Input</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        form { margin: auto; width: 50%; padding: 20px; border: 1px solid #ddd; border-radius: 10px; }
        input[type="text"], input[type="submit"] { padding: 10px; margin: 10px; }
        input[type="text"] { width: 80%; }
    </style>
</head>
<body>
    <h2>Enter Genomic Data</h2>
    <form action="/submit_data" method="post">
        <input type="text" name="data" placeholder="Enter genomic data" required>
        <br>
        <input type="submit" value="Store in Blockchain">
    </form>
    <br>
    <a href="/chain">View Blockchain</a>
</body>
</html>
"""

@app.route('/')
def index():
    """Renders the input form."""
    return render_template_string(HTML_FORM)

@app.route('/submit_data', methods=['POST'])
def submit_data():
    """Receives form input and adds it to the blockchain."""
    data = request.form.get("data")
    if not data:
        return "Error: Data is required!", 400

    new_block = blockchain.add_block(data)
    return f"<h3>Block {new_block.index} added!</h3><a href='/'>Go Back</a>"

# 🌐 API Endpoints
@app.route('/add_data', methods=['POST'])
def add_data():
    """Encrypts and stores genomic data in a new block."""
    data = request.json.get("data")
    if not data:
        return jsonify({"error": "Data is required"}), 400
    
    new_block = blockchain.add_block(data)
    return jsonify({
        "message": "Block added!",
        "index": new_block.index,
        "hash": new_block.hash
    }), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    """Returns the entire blockchain."""
    return jsonify({"chain": blockchain.get_chain()}), 200

# 🔨 Run Flask Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
