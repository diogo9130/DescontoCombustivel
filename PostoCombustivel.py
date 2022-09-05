preco_litro_gasolina = 5.30
preco_litro_alcool = 4.90
gasolina = "G"
alcool = "A"

print("Bem vindo ao sistema de desconto de combustíveis!!!\n\nTabela de preços\n\nLitro da Gasolina: 5.30R$"
      "\nLitro do Álcool: 4.90R$\n\nTabela de descontos\n\nÁlcool:\nIgual ou abaixo de 20 litros 3% de desconto"
      "\nAcima de 20 litros 5% de desconto\n\nGasolina: \nIgual ou abaixo de 20 litros 4% de desconto\nAcima de 20 litros"
      " 6% de desconto")

tipo_combustivel = input("\nInsira o tipo do combutível:\nG - gasolina\nA - alcool\n\n")

while tipo_combustivel != gasolina and tipo_combustivel != alcool:
  tipo_combustivel = input("\nTipo de combustível inválido. Insira o tipo do combutível:\nG - gasolina\nA - alcool\n\n")

quantidade_litros = int(input("\nInsira a quantidade de litros:\n"))

if quantidade_litros <= 20 and tipo_combustivel == "A":
  desconto = quantidade_litros * preco_litro_alcool / 100 * 3
  total_a_pagar = quantidade_litros * preco_litro_alcool + desconto
  print(f"\nTotal à pagar: {total_a_pagar} R$")

elif quantidade_litros > 20 and tipo_combustivel == "A":
  desconto = quantidade_litros * preco_litro_alcool / 100 * 5
  total_a_pagar = quantidade_litros * preco_litro_alcool + desconto
  print(f"\nTotal à pagar: {total_a_pagar} R$")

elif quantidade_litros <=20 and tipo_combustivel == "G":
  desconto = quantidade_litros * preco_litro_gasolina / 100 * 4
  total_a_pagar = quantidade_litros * preco_litro_gasolina + desconto
  print(f"\nTotal à pagar: {total_a_pagar} R$")

else:
  desconto = quantidade_litros * preco_litro_gasolina / 100 * 6
  total_a_pagar = quantidade_litros * preco_litro_gasolina + desconto
  print(f"\nTotal à pagar: {total_a_pagar} R$")





