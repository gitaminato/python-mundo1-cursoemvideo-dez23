#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

x = input('Digite algo: ')
print('O tipo primitivo é ', type(x))
print('É composto por uma letra e um número? ', x.isalnum())
print('É uma letra? ', x.isalpha())
print('É um dígito? ', x.isdigit())
print('É um decimal? ', x.isdecimal())
print('É um identificador? ', x.isidentifier())
print('Está escrito em minúsculo? ', x.islower())
print('É um número? ', x.isnumeric())
print('É um título? ', x.istitle())
print('É um espaço? ', x.isspace())
print('Está em maiúsculo? ', x.isupper())
print('É um ASCII 0 American Standard Code for Information Interchange? ', x.isascii())
