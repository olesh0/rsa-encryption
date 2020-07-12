from math import sqrt
from itertools import count, islice

import rsa_sender_decode_message

def is_prime(n):
  return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

def main():
  first_simple_number = int(input('First simple number: '))
  second_simple_number = int(input('Second simple number: '))

  public_key = first_simple_number * second_simple_number
  fi = (first_simple_number - 1) * (second_simple_number - 1)
  
  exponent = 1

  while True:
    division_change = fi % exponent

    if is_prime(exponent) and division_change is not 0:
      break

    exponent += 1

  secret_exponent = get_secret_exponent(fi=fi, e=exponent)

  print('-------')
  print(f'exponent: {exponent}')
  print(f'fi: {fi}')
  print(f'public key: {public_key}')
  print(f'secret exponent: {secret_exponent}')
  print('------ PASS exponent and public_key to your partner')

  rsa_sender_decode_message.decode(public_key=public_key, secret_exponent=secret_exponent)

def get_secret_exponent(fi, e):
  k = 1
  secret = None

  while True:
    check = (fi * k + 1) / e

    if check == int(check):
      secret = int(check)
      break
    else:
      print(f'fail... k={k}')
      k += 1

  print(f'd is found. d={secret}')

  return secret

if __name__ == '__main__':
  main()