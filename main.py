#Password Generator Project


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passw = ''

for i in range(0,nr_letters):
  letters_ = random.choice(letters)
  passw+=letters_
for i in range(0,nr_symbols):
  symbols_ = random.choice(symbols)
  passw+=symbols_
for i in range(0,nr_numbers):
  numbers_ = random.choice(numbers)
  passw+=numbers_


sample = []
for i in passw:
  sample.append(i)
random.shuffle(sample)

password=''
for i in sample :
  password+=i

print(f"Your password is : {password}")
