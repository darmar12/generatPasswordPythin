import random
litterSmall = 'abcdefghijklnopqrstuvwxyz'
litterBig = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
symbols = '+-/*!&$#?=@<>'
chars = ''
length = input("Length of password?" + "\n")
length = int(length)
password = ""
for partPass in range(length):
    password += random.choice(chars)
print(password)