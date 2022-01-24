compras = []
resp = "s"
while resp != "n":
    compras.append(input("Digite o item da lista: "))
    resp = input ("Deseja continuar - s para Sim ou n para Não: ")
for x in compras:
    if x == "banana":
        print("Encontrei a banana!!!")
    else:
        print("Não encontrei a banana!")
        
