print('Bem-vindo a Mariana Dall Alba Pizzaria!')
print('|-----------------------------------------------------------|')
print('|                          CARDÁPIO:                        |')
print('|-----------------------------------------------------------|')
print('| Código |  Descrição   | Pizza Média (M) | Pizza Grande (G)|')
print('|   21   |  Napolitana  |    R$ 20,00     |    R$ 26,00     |')
print('|   22   |  Margherita  |    R$ 20,00     |    R$ 26,00     |')
print('|   23   |  Calabresa   |    R$ 25,00     |    R$ 32,50     |')
print('|   24   |  Toscana     |    R$ 30,00     |    R$ 39,00     |')
print('|   25   |  Portuguesa  |    R$ 30,00     |    R$ 39,00     |')
print('|-----------------------------------------------------------|')

valor = 0
while True:
  tamanho = input('Qual o tamanho da pizza?')
  if(tamanho == 'M'):
    break
  elif(tamanho == 'G'):
    break
  else:
    print('Opção inválida.')
    continue

while True:  
  sabor = input('Qual o código do sabor da pizza?')
  if(sabor == '21' and tamanho == 'M' or sabor =='22' and tamanho == 'M'):
    valor = valor + 20
  elif(sabor == '21' and tamanho == 'G' or sabor =='22' and tamanho == 'G'):
    valor = valor + 20 * 1.3
  elif(sabor == '23' and tamanho == 'M'):
    valor = valor + 25
  elif(sabor == '23' and tamanho == 'G'):
    valor = valor + 25 * 1.3
  elif(sabor == '24' and tamanho == 'M' or sabor =='25' and tamanho == 'M'):
    valor = valor + 30
  elif(sabor == '24' and tamanho == 'G' or sabor =='25' and tamanho == 'G'):
    valor = valor + 30 * 1.3
  else:
    print('Opção inválida.')
    continue
  outro = input('Deseja pedir mais alguma coisa? (Sim/Não)')
  if(outro == 'Sim'):
    tamanho = input('Qual o tamanho da pizza?')
  elif(outro == 'Não'):
    print('O valor final é de {} reais.' .format(valor))
    break