from user import User

def main():
    print("Secure Messaging App (RSA Encrypted)\n")

    # Create users
    user1 = User("Alice")
    user2 = User("Bob")

    print("Public keys exchanged securely.")
    print(f"Alice's Public Key: {user1.get_public_key()[:50]}...")
    print(f"Bob's Public Key: {user2.get_public_key()[:50]}...\n")

    while True:
        print("Choose an action:")
        print("1. Alice sends message to Bob")
        print("2. Bob sends message to Alice")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            msg = input("Enter message from Alice to Bob: ")
            encrypted = user1.encrypt_for(user2.get_public_key(), msg)
            print(f"Encrypted Message: {encrypted}")
            decrypted = user2.decrypt_message(encrypted)
            print(f"Bob received and decrypted: {decrypted}\n")

        elif choice == '2':
            msg = input("Enter message from Bob to Alice: ")
            encrypted = user2.encrypt_for(user1.get_public_key(), msg)
            print(f"Encrypted Message: {encrypted}")
            decrypted = user1.decrypt_message(encrypted)
            print(f"Alice received and decrypted: {decrypted}\n")

        elif choice == '3':
            print("Exiting Secure Messaging App.")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
