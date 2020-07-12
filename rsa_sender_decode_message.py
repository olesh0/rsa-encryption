def main():
  secret_exponent = int(input('Your secret exponent: '))
  public_key = int(input('Your public key: '))

  decode(
    secret_exponent=secret_exponent,
    public_key=public_key
  )

def decode(secret_exponent, public_key):
  cipher_text = int(input('Received cipher text: '))
  decoded = pow(cipher_text, secret_exponent) % public_key

  print(f'Decoded message is {decoded}')

if __name__ == '__main__':
  main()