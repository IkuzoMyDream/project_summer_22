import random

print('Welcome to your password generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()<>,.ฺ/?"'';:"[]{}=-_+*&฿^%$#@!'

number = int(input('Amount of password to generate: '))

lenght = int(input('Input your password lenght: '))

print('Here our pass word: ')

for pwd  in range(number):
    password = ''
    for c in range(lenght):
        password += random.choice(chars)
    print(password)

