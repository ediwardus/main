a = 'A'
b = 'B'
c = 1.1
formato = 'a={} b={} c={}'.format(a, b, c)
formato2 = 'a={2} b={1} c={0}'.format(a, b, c)
formato3 = 'a={nome1} b={nome2} c={nome3}'.format(nome1=a, nome2=b, nome3=c)
print(formato)
print(formato2)
print(formato3)
print(formato2+formato)
print(3*formato)
