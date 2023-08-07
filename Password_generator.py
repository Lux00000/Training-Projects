import random

chars = 'dskjmgsd;dmgkl1954823-52398&%^*&)()($*@)'
number = input('count of generations'+ "\t")
length = input('lenght of password'+ "\t")

number = int(number)
length = int(length)

for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)


