import client
import client_crypto

def main():
    client.GetServerKey()
    key = client_crypto.GetServerRSAKey()
    print(str(client_crypto.ServerKey_toText(key)))

if __name__ == "__main__":
    
    main()
    #cipher_key = Fernet.generate_key() #get_key()


    #print("Enter your SUPER(super-super) secret text: ")
    #msg = input()
    #enc_text = encrypt(cipher_key, msg)
    #print(str(enc_text))
    #original = decrypt(cipher_key, enc_text)
    #print("\n\n" + original)