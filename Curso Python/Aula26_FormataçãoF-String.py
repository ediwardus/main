"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
print(variavel)

"""
As f-strings são uma forma mais moderna e eficiente de formatar strings. 
As f-strings são úteis por:
Economizarem tempo e código 
Permitirem a inserção de expressões dentro de strings 
Permitirem formatar com casa decimal, como moeda, percentual, datas, entre outros 
Permitirem abrir um arquivo e dentro do corpo de um e-mail 
Permitirem o uso de funções Lambda 
Para usar uma f-string, basta colocar a letra "f" antes do texto 
e colocar a variável dentro de chaves. 
Por exemplo, para imprimir "Meu nome é {nome} e tenho {idade} anos", 
pode-se usar o código: 
"""

nome = "João"
idade = 30
print(f"Meu nome é {nome} e tenho {idade} anos. ")

