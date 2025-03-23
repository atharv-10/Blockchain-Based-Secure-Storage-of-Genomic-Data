from blockchain import Blockchain

blockchain = Blockchain()

while True:
    print("\n🔹 Encrypted Blockchain Data Storage 🔹")
    print("1. Add Data to Blockchain")
    print("2. View Blockchain")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = input("Enter data to store: ")
        block_hash = blockchain.add_block(data)
        print(f"✅ Data added! Block Hash: {block_hash}")

    elif choice == "2":
        for block in blockchain.get_chain():
            print("\n📦 Block:")
            print(f"Index: {block['index']}")
            print(f"Previous Hash: {block['previous_hash']}")
            print(f"🔐 Encrypted Data: {block['encrypted_data']}")
            print(f"🔓 Decrypted Data: {block['decrypted_data']}")
            print(f"Timestamp: {block['timestamp']}")
            print(f"Hash: {block['hash']}\n")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("❌ Invalid choice. Try again.")
