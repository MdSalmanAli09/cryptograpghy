from rsa_utils import generate_keys, encrypt_message, decrypt_message

class User:
    def __init__(self, name):
        self.name = name
        self.private_key, self.public_key = generate_keys()

    def get_public_key(self):
        return self.public_key

    def encrypt_for(self, recipient_public_key, message):
        return encrypt_message(recipient_public_key, message)

    def decrypt_message(self, encrypted_message):
        return decrypt_message(self.private_key, encrypted_message)
