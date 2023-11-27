from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


def generate_keys():
    # Generate the RSA public/private key pair
    rsa_key_pair = RSA.generate(2048)

    # Output Private Key
    private_key = rsa_key_pair.export_key()
    print(private_key)
    with open("my_private.pem", "wb") as out_file:
        out_file.write(private_key)

    # Output Public Key
    public_key = rsa_key_pair.publickey().export_key()
    print(public_key)
    with open("my_public.pem", "wb") as out_file:
        out_file.write(public_key)


def encrypt():
    # Secret data to be sent
    data = "CIA classified info".encode("utf-8")

    # Generate a random key to use for symmetric encryption with AES
    aes_key = get_random_bytes(16)

    # Encrypt secret data with AES
    aes_encoder = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = aes_encoder.encrypt_and_digest(data)

    # Need to send aes_key and cipher text to recipient.
    # But, if I send both and message intercepted, user could decrypt using
    #   the sent aes_key.
    # So, encrypt aes_key with asymmetric encryption that only recipient
    #   can decrypt

    # Get recipient public key
    recipient_public_key = RSA.import_key(
      open("kyle_public.pem", 'rb').read())

    # Use recipient public key to asymmetrically encode the aes_key
    rsa_encoder = PKCS1_OAEP.new(recipient_public_key)
    encrypted_aes_key = rsa_encoder.encrypt(aes_key)

    # Place needed data into file to send
    with open("encrypted_data_to_send.bin", 'wb') as out_file:
        [out_file.write(x) for x in (encrypted_aes_key,
                                     aes_encoder.nonce,
                                     tag,
                                     ciphertext)]


def decrypt():
    # Load in your private key
    with open("my_private.pem", 'rb') as in_file:
        private_key = RSA.import_key(in_file.read())

    # Read-in data from the received file
    with open("encrypted_data.bin", 'rb') as in_file:
        encrypted_aes_key = in_file.read(private_key.size_in_bytes())
        nonce = in_file.read(16)
        tag = in_file.read(16)
        ciphertext = in_file.read()

    # Decrypt the AES key with the private key
    rsa_decoder = PKCS1_OAEP.new(private_key)
    code_word = rsa_decoder.decrypt(encrypted_aes_key)
    print(code_word.decode("utf-8"))

    """
    # Decrypt the data with the AES session key
    aes_decoder = AES.new(aes_key, AES.MODE_EAX, nonce)
    data = aes_decoder.decrypt_and_verify(ciphertext, tag)
    print(data.decode("utf-8"))
    """


decrypt()


