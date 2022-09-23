quant= int(input('Digite a quantidade de numeros: '))
lista=[]
i=1

while i<= int(quant):
    numero=input('Digite o número: ')
    lista.append(numero)
    i +=1

def maior(lista):
    maior = lista[0]
    for num in lista:
        if (num > maior):
            maior=num
    return maior

def menor(lista):
    menor = lista[0]
    for num2 in lista:
        if (num2 < menor):
            menor=num2
    return menor

print('O maior valor é:', maior(lista))
print('O menor valor é:', menor(lista))



