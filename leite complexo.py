print()
comprador = 0
lista = []
leite = 0
print("Bem vindo! O primeiro passo é digitar o preço do leite.")
print()
leite = float(input("Quando custa 1 litro de leite? : "))
print()
print("Perfeito! Agora escreva o nome dos compradores. Quando quiser parar digite Pronto")
print()
while comprador != 1:
    comprador = str(input("Insira o nome do comprador: "))
    lista.append(comprador)
    if comprador == ("Pronto"):
        comprador = 1
lista.pop()
nin = len(lista)
cres = 0
leicomp = 0
lisint = ()
lisfin = []
valortotal = float()
while nin != cres:
    leicomp = float(input(f"Quantos litros de leite {lista[cres]} comprou? : "))
    leicomp *= leite
    lisint = (f"{lista[cres]} pagou R${leicomp}")
    lisfin.append(lisint)
    valortotal += leicomp
    leitecomp = 0
    lisint = ()
    cres += 1
for i in range(5):
    print()
print(lisfin)
print()
print(f"Seu lucro total foi de R${valortotal}")
for i in range(3):
    print()