# Blockchain-Based-Secure-Storage-of-Genomic-Data
A blockchain-based storage system that ensures integrity, security, and decentralization. Our approach leverages AES encryption for data privacy, Proof-of-Work (PoW) consensus for integrity, and Flask-based APIs for accessibility. The system is deployed on AWS, making it scalable and publicly accessible.


Blockchain-Based Genomic Data Storage 🚀
A secure blockchain-based system for storing genomic data using AES encryption and Proof-of-Work consensus, deployed on AWS EC2.

📌 Features
✅ Immutable Storage: Data is permanently stored using blockchain.
✅ AES-256 Encryption: Ensures genomic data privacy.
✅ Proof-of-Work (PoW): Prevents tampering and unauthorized modifications.
✅ Flask-based REST API: For easy interaction with the blockchain.
✅ AWS Deployment: Ensures scalability and accessibility.

📂 Project Structure

blockchain_project/
│── blockchain.py        # Blockchain class for managing the chain
│── app.py               # Flask API for data input & retrieval
│── keygen.py            # AES key generation utility
│── sign_transaction.py  # Digital signature implementation
│── test_encrypt.py      # Testing AES encryption
│── requirements.txt     # Required Python libraries
│── README.md            # Project documentation
│── private_key.pem      # Private key for encryption (DO NOT SHARE)
│── public_key.pem       # Public key for decryption
│── venv/                # Virtual environment (not included in repo)

📦 Installation

1️⃣ Clone the repository
git clone 
cd to the repo

2️⃣ Set up a virtual environment
python3 -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install dependencies
pip install -r requirements.txt
🚀 Running the Blockchain
Start the Flask Server
python app.py --host=0.0.0.0 --port=5000

The API will be accessible at:
👉 http://127.0.0.1:5000/ (Localhost)
👉 http://YOUR_AWS_IP:5000/ (AWS Deployment)

📡 API Endpoints
Endpoint	Method	Description
/	GET	Web interface for genomic data input
/submit_data	POST	Encrypts and adds data to blockchain
/mine	GET	Mines a new block
/chain	GET	Retrieves the full blockchain
Example API Call (Submit Data)

curl -X POST http://127.0.0.1:5000/submit_data -H "Content-Type: application/json" -d '{"data":"AGCTCGT"}'
🔒 Security Features
🔹 AES-256 Encryption: Encrypts genomic data before storing in blockchain.
🔹 SHA-256 Hashing: Ensures integrity of stored blocks.
🔹 Proof-of-Work (PoW): Prevents unauthorized modifications.

🌍 Deployment on AWS
1️⃣ Connect to EC2

ssh -i "blockchain-key.pem" ubuntu@your-aws-ip

2️⃣ Install Python & Dependencies

sudo apt update
sudo apt install python3 python3-pip python3-venv -y

3️⃣ Run Flask Server

source venv/bin/activate
python app.py --host=0.0.0.0 --port=5000

4️⃣ Update Security Rules
✔ Allow inbound traffic for Port 5000 in AWS Security Group.
