username = 'admin'
password = '1234'

DigitUser = input('Digite o usuário: ')
DigitPass = input('Digite a senha: ')

if(DigitUser == username and DigitPass == password ):
  print('Login realizado com sucesso')
  print('Bem-vindo ao sistema')
else:
  print('Usuário ou senha incorretos')
