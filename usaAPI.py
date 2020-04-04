import API

a = API.Conjunto()
b = API.Conjunto()

a.insereNome('A')

b.insereNome('B')

a.inserir('1')
a.inserir('2')
a.inserir('3')
a.inserir('4')

b.inserir('1')
b.inserir('2')


print('Complemento :', a.complemento(b))

'''A = 1 2 3 4

   B = 1 2      '''
