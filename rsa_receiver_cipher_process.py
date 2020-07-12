def main():
  exponent = int(input('The exponent: '))
  public_key = int(input('Public key: '))
  secret_message = int(input('3 digit number to transfer: '))

  cipher_message = pow(secret_message, exponent) % public_key

  print(cipher_message)

if __name__ == '__main__':
  main()